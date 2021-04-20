aa_list = (("A", "Ala", "Alanine"),
           ("C", "Cys", "Cystein"),
           ("D", "Asp", "Aspartate"),
           ("E", "Glu", "Glutamate"),
           ("F", "Phe", "Phenylalanine"),
           ("G", "Gly", "Glycine"),
           ("H", "His", "Histidine"),
           ("I", "Ile", "Isoleucine"),
           ("K", "Lys", "Lysine"),
           ("L", "Leu", "Leucine"),
           ("M", "Met", "Methionine"),
           ("N", "Asn", "Asparagine"),
           ("P", "Pro", "Proline"),
           ("Q", "Gln", "Glutamine"),
           ("R", "Arg", "Arginine"),
           ("S", "Ser", "Serine"),
           ("T", "Thr", "Threonine"),
           ("V", "Val", "Valine"),
           ("W", "Trp", "Tryptophan"),
           ("Y", "Tyr", "Tyrosine")
          )
# https://www.geeksforgeeks.org/dna-protein-python-3/
tr_list = {
           'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
           'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
           'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
           'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
           'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
           'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
           'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
           'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
           'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
           'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
           'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
           'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
           'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
           'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
           'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
           'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
          }

aa_info = {'A': {'formula': 'C3H7NO2',
                 'smiles': 'O=C(O)C(N)C',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': 1.8,
                 'essential': 'nonessential',
                 'pI': 6.01,
                 'pK1': 2.35,
                 'pK2': 9.87},
           'R': {'formula': 'C6H14N4O2',
                 'smiles': 'O=C(O)C(N)CCC/N=C(\\N)N',
                 'polarity': 'polar',
                 'charge': 'positive',
                 'hydropathy_index': -4.5,
                 'essential': 'essential',
                 'pI': 10.76,
                 'pK1': 1.82,
                 'pK2': 8.99},
           'N': {'formula': 'C4H8N2O3',
                 'smiles': 'O=C(N)C[C@H](N)C(=O)O',
                 'polarity': 'polar',
                 'charge': 'neutral',
                 'hydropathy_index': -3.5,
                 'essential': 'nonessential',
                 'pI': 5.41,
                 'pK1': 2.14,
                 'pK2': 8.72},
           'D': {'formula': 'C4H7NO4',
                 'smiles': 'O=C(O)CC(N)C(=O)O',
                 'polarity': 'polar',
                 'charge': 'negative',
                 'hydropathy_index': -3.5,
                 'essential': 'nonessential',
                 'pI': 2.85,
                 'pK1': 1.99,
                 'pK2': 9.9},
           'C': {'formula': 'C3H7NO2S',
                 'smiles': 'C([C@@H](C(=O)O)N)S',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': 2.5,
                 'essential': 'nonessential',
                 'pI': 5.05,
                 'pK1': 1.92,
                 'pK2': 10.7},
           'E': {'formula': 'C5H9NO4',
                 'smiles': 'C(CC(=O)O)C(C(=O)O)N',
                 'polarity': 'polar',
                 'charge': 'negative',
                 'hydropathy_index': -3.5,
                 'essential': 'nonessential',
                 'pI': 3.15,
                 'pK1': 2.1,
                 'pK2': 9.47},
           'Q': {'formula': 'C5H10N2O3',
                 'smiles': 'O=C(N)CCC(N)C(=O)O',
                 'polarity': 'polar',
                 'charge': 'neutral',
                 'hydropathy_index': -3.5,
                 'essential': 'nonessential',
                 'pI': 5.65,
                 'pK1': 2.17,
                 'pK2': 9.13},
           'G': {'formula': 'C2H5NO2',
                 'smiles': 'C(C(=O)O)N',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': -0.4,
                 'essential': 'nonessential',
                 'pI': 6.06,
                 'pK1': 2.35,
                 'pK2': 9.78},
           'H': {'formula': 'C6H9N3O2',
                 'smiles': 'O=C(O)[C@@H](N)Cc1cncn1',
                 'polarity': 'polar',
                 'charge': 'neutral',
                 'hydropathy_index': -3.2,
                 'essential': 'essential',
                 'pI': 7.6,
                 'pK1': 1.8,
                 'pK2': 9.33},
           'I': {'formula': 'C6H13NO2',
                 'smiles': 'CC[C@H](C)[C@@H](C(=O)O)N',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': 4.5,
                 'essential': 'essential',
                 'pI': 6.05,
                 'pK1': 2.32,
                 'pK2': 9.76},
           'L': {'formula': 'C6H13NO2',
                 'smiles': 'CC(C)C[C@@H](C(=O)O)N',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': 3.8,
                 'essential': 'essential',
                 'pI': 6.01,
                 'pK1': 2.33,
                 'pK2': 9.74},
           'K': {'formula': 'C6H14N2O2',
                 'smiles': 'C(CCN)CC(C(=O)O)N',
                 'polarity': 'polar',
                 'charge': 'positive',
                 'hydropathy_index': -3.9,
                 'essential': 'essential',
                 'pI': 9.6,
                 'pK1': 2.16,
                 'pK2': 9.06},
           'M': {'formula': 'C5H11NO2S',
                 'smiles': 'CSCCC(C(=O)O)N',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': 1.9,
                 'essential': 'essential',
                 'pI': 5.74,
                 'pK1': 2.13,
                 'pK2': 9.28},
           'F': {'formula': 'C9H11NO2',
                 'smiles': 'c1ccc(cc1)C[C@@H](C(=O)O)N',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': 2.8,
                 'essential': 'essential',
                 'pI': 5.49,
                 'pK1': 2.2,
                 'pK2': 9.31},
           'P': {'formula': 'C5H9NO2',
                 'smiles': 'C1CC(NC1)C(=O)O',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': -1.6,
                 'essential': 'nonessential',
                 'pI': 6.3,
                 'pK1': 1.95,
                 'pK2': 10.64},
           'S': {'formula': 'C3H7NO3',
                 'smiles': 'C([C@@H](C(=O)O)N)O',
                 'polarity': 'polar',
                 'charge': 'neutral',
                 'hydropathy_index': -0.8,
                 'essential': 'nonessential',
                 'pI': 5.68,
                 'pK1': 2.19,
                 'pK2': 9.21},
           'T': {'formula': 'C4H9NO3',
                 'smiles': 'C[C@H]([C@@H](C(=O)O)N)O',
                 'polarity': 'polar',
                 'charge': 'neutral',
                 'hydropathy_index': -0.7,
                 'essential': 'essential',
                 'pI': 2.09,
                 'pK1': 2.09,
                 'pK2': 9.1},
           'W': {'formula': 'C11H12N2O2',
                 'smiles': 'c1ccc2c(c1)c(c[nH]2)C[C@@H](C(=O)O)N',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': -0.9,
                 'essential': 'essential',
                 'pI': 5.89,
                 'pK1': 2.46,
                 'pK2': 9.41},
           'Y': {'formula': 'C9H11NO3',
                 'smiles': 'N[C@@H](Cc1ccc(O)cc1)C(O)=O',
                 'polarity': 'polar',
                 'charge': 'neutral',
                 'hydropathy_index': -1.3,
                 'essential': 'nonessential',
                 'pI': 5.64,
                 'pK1': 2.2,
                 'pK2': 9.21},
           'V': {'formula': 'C5H11NO2',
                 'smiles': 'CC(C)[C@@H](C(=O)O)N',
                 'polarity': 'nonpolar',
                 'charge': 'neutral',
                 'hydropathy_index': 4.2,
                 'essential': 'essential',
                 'pI': 6.0,
                 'pK1': 2.39,
                 'pK2': 9.74}}

def aa1_to_aa3(letter):
    return {a: b for a,b,c in aa_list}[letter]

def aa3_to_aa1(word):
    return {b: a for a,b,c in aa_list}[word]

def aa1_to_name(letter):
    return {a: c for a,b,c in aa_list}[letter]

def aa3_to_name(word):
    return {b: c for a,b,c in aa_list}[word]

def codon_from_aa(letter):
    codon = {l: [n for j,n in [(v, k) for k,v in tr_list.items()] if j == l]
             for l in set([v for k,v in tr_list.items()])}[letter]
    return codon


class AminoAcid:

    def __init__(self, name):
        if len(name) == 1:
            if name not in [a[0] for a in aa_list]:
                aa_prompt = "\n".join([a[0]+ " -> " + a[2] for a in aa_list])
                raise NameError("Invalid letter. Only 20 common "
                                "amino-acids:\n" + aa_prompt)
            self.name = aa1_to_name(name)
            self.symbol = name
            self.symbol3 = aa1_to_aa3(name) 
        elif len(name) == 3:
            if name not in [a[1] for a in aa_list]:
                aa_prompt = "\n".join([a[1]+ " -> " + a[2] for a in aa_list])
                raise NameError("Invalid three-letter code. Only 20 common "
                                "amino-acids:\n"+ aa_prompt)
            self.name = aa3_to_name(name)
            self.symbol3 = name
            self.symbol = aa3_to_aa1(name)

        else:
            raise ValueError("Please enter amino-acid symbol"
                             " (1 or 3 letters).")
        self.random_probability = len(codon_from_aa(self.symbol))/64

        if self.symbol in "DE":
            self.charge_at_ph7 = -1
            self.polar = True
        elif self.symbol in "HKR":
            self.charge_at_ph7 = 1
            self.polar = True
        else:
            self.charge_at_ph7 = 0
            if self.symbol in "CGNQSTY":
                self.polar = True
            else:
                self.polar = False
        
        self.codon = codon_from_aa(self.symbol)
        self.formula = aa_info[self.symbol]["formula"]
        self.smiles = aa_info[self.symbol]["smiles"]
        self.hidropathy = aa_info[self.symbol]["hydropathy_index"]
        self.essential = aa_info[self.symbol]["essential"]
        self.pI = aa_info[self.symbol]["pI"]
        self.pK1 = aa_info[self.symbol]["pK1"]
        self.pK2 = aa_info[self.symbol]["pK2"]
    
    def __repr__(self):
        return self.name

