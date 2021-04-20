"""
Uniprot, a set of functionalities to obtain information from www.uniprot.org

Classes:
Uniprot -- take an Uniprot ID and get some information (sequence, function...).

Imports:
requests -- Useful for dealing with HTTP requests.
bs4 -- Helps in parsing the webpages to be searched.
time -- Necessary for crawler delay implementations (in Uniprot, 3s [default]).
re -- To extract information with Regular Expressions.
"""
import requests
from bs4 import BeautifulSoup as bs
import time
import re

def rm_sup_from_bs(soup):
    page = str(soup)
    pattern = "(<sup>.*</sup>)"

    while re.search(pattern, page) is not None:
        start = re.search(pattern, page).start()
        end = re.search(pattern, page).end()
        page = page[:start] + page[end:]
    
    soup = bs(page, "html.parser")

    return soup

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
        self.load()

    def load(self):
        """Fetch Uniprot when the class is created. Create some instance
        variables such as basic information (protein, gene, organism, status),
        function (including GO annotations) and sequence of the Uniprot entry.
        """

        url = "https://www.uniprot.org/uniprot/{}".format(self.id.upper())
        page = requests.get(url).text
        self.soup = bs(page, "html.parser")
        self.seq = self._find_seq()
        self.function = self._find_function()
        self.basic_info = self._find_basic_info()
        self.go = self._find_go_annot()
        self.sites = self._find_sites()
    
    def _find_seq(self):
        """Find the sequence of an entry in Uniprot given the BeautifulSoup
        object resulting from parsing the webpage of the entry. Return the
        sequence in FASTA format (Uniprot ID is set as header) as a string.
        """

        seq = self.soup.find("pre", {"class": "sequence"}).text
        for char in " 0123456789":
            seq = seq.replace(char, "")
        return ">{}\n{}".format(self.id, seq)

    def _find_function(self):
        """Find the function description of an entry in Uniprot given the
        BeautifulSoup object resulting from parsing the webpage of the entry.
        The PubMed references are removed from function instance variable and
        stored in another instance variable (pubmed_refs). Return the function
        description as a string.
        """

        func = self.soup.find("div", {"id": "function"})
        func_text1 = func.findAll("div", {"class": "annotation"})[0]
        func1_cur = func_text1.text[:func_text1.text.find(func_text1.span.find("span").text)]        

        pubmed = "(PubMed:\d+)"
        self.pubmed_refs = []
        while re.search(pubmed, func1_cur) is not None:
            search = re.search(pubmed, func1_cur)
            start = search.start()
            end = search.end()
            self.pubmed_refs.append(func1_cur[start:end])
            
            func1_cur = func1_cur[:start] + func1_cur[end:]
        
        empty_par = "(\s?\(\W*\))"
        while re.search(empty_par, func1_cur) is not None:
            start = re.search(empty_par, func1_cur).start()
            end = re.search(empty_par, func1_cur).end()
            func1_cur = func1_cur[:start] + func1_cur[end:]
        return func1_cur

    def _find_basic_info(self):
        """Find basic information about the Uniprot entry: name of the protein,
        name of the gene, organism where it is expressed and status (reviewed
        or not). Return a dictionary with these data.
        """

        basic_info = {}
        for thing in ("protein", "gene", "organism", "status"):
            prompt = self.soup.find("div", {"id": "content-"+thing})
            if thing == "status":
                basic_info[thing] = prompt.a.text
                continue
            basic_info[thing] = prompt.text
        return basic_info

    def _find_go_annot(self):
        """Find Gene Ontology annotations of the Uniprot entry. There are three
        types of GO annotations: molecular functions, biological processes and
        subcellular location where the protein is expressed. Returns a 
        dictionary with this information.
        """
        go = {}

        mol_func_tag = self.soup.find("ul",
            {"class": "molecular_function"}).findAll("li")
        go["molecular_function"] = [li.a.text 
            for li in mol_func_tag if "GO/term" in li.a.get("href")]

        bio_proc_tag = self.soup.find("ul",
            {"class": "biological_process"}).findAll("li")
        go["biological_process"] = [li.a.text
            for li in bio_proc_tag if "GO/term" in li.a.get("href")]

        sub_loca_tag = [li for li in self.soup.find("div",
            {"class": "go terms"}).findAll("a") if len(li.text) > 0]
        go["subcellular_location"] = [a.text 
            for a in sub_loca_tag if "term/GO" in a.get("href")]

        return go

    def _find_sites(self):
        sites = {}
        function = self.soup.find("div", {"id": "function"})
        sites_table = function.table.findAll("tr")[1:]
        for tr in sites_table:
            tds = tr.findAll("td")
            if "display:none" in str(tr):
                kind = rm_sup_from_bs(tds[0]).text.split(">")[-1]
                
            else:
                kind = rm_sup_from_bs(tds[0]).text
            resi = tds[1].text
            importance = tds[2].span.text
            sites[resi] = (kind, importance)
        
        return sites

    def __repr__(self):
        info = [self.id.upper()] + list(self.basic_info.values())[:-1]
        return ("Entry: {}\nProtein: {}\nGene: {}\nOrganism: {}"
                "".format(info[0], info[1], info[2], info[3]))



