##Imports
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
import re
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def pdb_to_pandas(pdb):
    patt = ("ATOM\s+(\d+)\s+(\w+)\s+(\w+)\s+(\w)\s*(\d+)"
            "\s*([\-\d]+\.\d{3})\s*([\-\d]+\.\d{3})\s*([\-\d]+\.\d{3})"
            "\s*(\d\.\d{2})\s*([\d\.]+)")
    table = [re.search(patt, pos).groups() for pos in pdb.split("\n") 
             if pos.startswith("ATOM")]
    columns = ("atom_id", "atom_name", "res_name", "chain", "res_id",
               "x", "y", "z", "occupancy", "b_factor")
    df= pd.DataFrame(table, columns = columns)
    df = df.astype({
            "atom_id": int,
            "atom_name": str,
            "res_name": str,
            "chain": str,
            "res_id": int,
            "x": float,
            "y": float,
            "z": float, 
            "occupancy": float,
            "b_factor": float
        })

    return df
    
    pass

class PDB:

    def __init__(self, thing):
        
        if len(thing) == 4:
            self.load_from_web(thing)
            self.table = pdb_to_pandas(self.page)
        elif len(thing) > 4:
            self.load_from_file(thing)
            self.table = pdb_to_pandas(self.page)
        else:
            print("Invalid input. Please try again")

    def load_from_file(self, file):
        with open(file, "r") as f:
            pdb = f.readlines().join("\n")

        return pdb

    def get_up_ids(self):
        pass

    def load_from_web(self, pdb_id):
        url = "https://files.rcsb.org/view/{}.pdb".format(pdb_id)
        self.page = requests.get(url).text

    def plot(self, sidechain = False, threshold = False):
        """
        Plot protein structure. Sidechain is a Boolean to select if sidechains
        are to be displayed (True) or not (False, default). Threshold (if set)
        is a three-elements tuple with:
        - [0]: mode, type of ID introduced at [1]. "R" for residue, "A" for 
           atom.
        - [1]: ID of the atom/residue.
        - [2]: distance to the corresponding atom/CA of residue.
        """

        df = self.table
        if not sidechain:   
            bb_atoms = [atom in ("N", "O", "C", "CA") for atom in df.atom_name]
            df = df[bb_atoms][["atom_name", "res_id", "x", "y", "z"]]
        
        if threshold:
            mode = threshold[0]
            ref_id = threshold[1]
            if mode == "R":
                ref_id = df[df["res_id"] == ref_id][df["atom_name"] == "CA"].head(n = 1).index
                       
            t = threshold[2]

            ref_coords = df.loc[ref_id][list("xyz")].values.reshape(-1,3)
            df["Dist"] = np.sqrt(np.sum(np.square(df[["x", "y", "z"]].values - ref_coords), axis = 1).astype(float))
            df = df[df["Dist"] < t]


        atom_colors = ["b"*a.count("N")+"r"*a.count("O")+"k"*a.count("C") 
                     for a in df.atom_name.to_list()]

        fig = plt.figure(figsize = (10, 7))
        ax = plt.axes(projection ="3d")
        ax.scatter3D(df.x, df.y, df.z, color = atom_colors)
        ax.plot(df.x, df.y, df.z, c = "k")
        plt.show()


