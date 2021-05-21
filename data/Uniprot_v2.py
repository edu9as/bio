import requests
from scrapy import Selector
import time
from math import ceil
import re

def get_all_uniprot_ids(query, output_file = False):
    
    if query.startswith("?query="):
        base_url = "https://www.uniprot.org/uniprot/{}&sort=score".format(query) + "{}"
    else:
        base_url = "https://www.uniprot.org/uniprot/?query={}&sort=score".format(query) + "{}"

    sel = Selector(requests.get(base_url.format("")))

    all_up_ids = set()
    results_xpath = '//strong[@class="queryResultCount"]/text()'

    results = int(sel.xpath(results_xpath).extract_first().replace(",",""))

    n_pages = ceil(results/25)
    print("Number of entries:", results, "",
          "Pages to request:", n_pages, "", "Expected time:", 
          f"{n_pages*3//3600}:{(n_pages*3%3600)//60}:{(n_pages*3%3600)%60}",
          "", "Pages fetched: ", sep = "\n")

    for i in range(n_pages):
        if i == 0:
            url = base_url.format("")
        else:
            url = base_url.format("&offset="+str(i*25))
        success = False
        while not success:
            try:
                time.sleep(3)
                sel = Selector(requests.get(url))
                success = True
            except:
                print("[oops]", end = ", ")
        
        all_up_ids.update(sel.xpath('//td[@class="entryID"]/a/text()').extract())
        
        if i % 20 == 19:
            print(i + 1, f"({len(all_up_ids)} entries so far)", end = ", ")
        else:
            print(i + 1, end = ", ")

    if output_file:
        with open(output_file, "w") as f:
            f.write("".join([str(n) + "\n" for n in all_up_ids]))


class Uniprot():
    """
    Class to get information from www.uniprot.org.

    Instance variables:
    basic_info -- Basic information about the Uniprot entry (dictionary).
    seq -- Protein sequence (string).
    function -- Protein function description (list of strings).
    go -- Gene Ontology annotations (dictionary).

    Public class methods:
    load -- Fetch www.uniprot.org when the Uniprot instance is created.
    """
    def __init__(self, thing):
        """Constructor of Uniprot class. Calls the load() method.
        
        Arguments:
        thing -- Uniprot ID to be fetched.
        """

        self.id = thing
        self._load()

    def _load(self):
        """Fetch Uniprot when the class is created. Create some instance
        variables such as basic information (protein, gene, organism, status),
        function (including GO annotations) and sequence of the Uniprot entry.
        """

        url = "https://www.uniprot.org/uniprot/{}".format(self.id.upper())
        self.page = Selector(requests.get(url))
        self.sequence = self._find_seq()
        self.description = self._find_descr()
        self.go = self._find_go_annot()
        self.basic_info = self._find_basic_info()
        self.pdb = self._find_pdb()
        self.sites = self._find_sites()
        """self.function = self._find_function()
        
        
        self.sites = self._find_sites()
    facts = {
    "GO_
    "description": '//div[@id="function"]/div[@class="annotation"]/span/text()',
    "sites": '//*[@id="sitesAnno_section"]/tr/td/span/text() | //*[@id="sitesAnno_section"]/tr/td/a/text()',
    
    "xrefs": '//*[@id="section_x-ref_phylogenomic"]/following-sibling::table//td/span/text() | //*[@id="section_x-ref_phylogenomic"]/following-sibling::table//td/a/@href',

}"""
    def _find_seq(self):
        """Find the sequence of an entry in Uniprot given the BeautifulSoup
        object resulting from parsing the webpage of the entry. Return the
        sequence in FASTA format (Uniprot ID is set as header) as a string.
        """
        xseq = '//pre[@class="sequence"]/text()'
        seq = "".join(self.page.xpath(xseq).extract())
        for char in " 0123456789":
            seq = seq.replace(char, "")
        seq = f">{self.id}\n{seq}"
        
        return seq

    def _find_descr(self):
        xdescr = '//div[@id="function"]/div[@class="annotation"]/span/text()'
        xrefs = '|//div[@id="function"]/div[@class="annotation"]/span/a/text()'
        self.pubmed = self.page.xpath(xrefs[1:]).extract()
        return "".join(self.page.xpath(xdescr+xrefs).extract())

    def _find_go_annot(self):
        xgo = {
            "mol_func": ('//div[@id="function"]//ul[@class="noNumbering '
                         'molecular_function"]/li/a/'),
            "bio_proc": ('//div[@id="function"]//ul[@class="noNumbering '
                         'biological_process"]/li/a/'),
            "sub_loca": '//div[@id="table-go_annotation"]//ul/li/a/'}
        go = {k: self.page.xpath(v + "text()").extract() for k,v in xgo.items()}
        ref = {k: self.page.xpath(v + "@href").extract() for k,v in xgo.items()}
        ref = {k: [n.split("/")[-1] for n in ref[k]] for k in ref.keys()}
        return {k: [*zip(go[k], ref[k])] for k in xgo.keys()}

    def _find_basic_info(self):
        xinfo = {
            "protein_name": '//*[@id="content-protein"]//text()',
            "gene_name": '//*[@id="content-gene"]//text()',
            "organism_name": '//*[@id="content-organism"]//text()'
        }
        return {k: self.page.xpath(v).extract()[0] for k,v in xinfo.items()}

    def _find_pdb(self):
        xpdb = '//a[@class="pdb"]//text()'
        return self.page.xpath(xpdb).extract()

    def _find_sites(self):
        xsites = ('//*[@id="sitesAnno_section"]/tr/td/span/text() |'
                  ' //*[@id="sitesAnno_section"]/tr/td/a/text()')
        sites = self.page.xpath(xsites).extract()
        #sites = [(sites[i], sites[i+1], sites[i+2]) for i in range(0,len(sites),3)]
        return sites