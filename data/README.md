# Bio data

In this folder I store some files with meaningful biological data:

- **almost_all_human_up.csv**: as a result of applying web scraping in UniProt domain, I gathered some data about roughly all human proteins in UniProt (status: reviewed). Columns are:
    - **Protein**: name of the protein.
    - **Gene**: name of the gene which encodes the protein.
    - **Species**: name of the species where the protein is expressed
    - **Description**: description of the protein in UniProt.
    - **GOMolFunc**: Gene Ontology annotations w.r.t. the molecular function of the protein. Format: this column is fromed by pairs of ```annotation```+```GO ID```; pairs are separated by &.
    - **GOBioProc**: Gene Ontology annotations w.r.t. the biological processes in which the protein participates. Format: this column is fromed by pairs of ```annotation```+```GO ID```; pairs are separated by &.
    - **GOSubLoc**: Gene Ontology annotations w.r.t. the subcellular locations where the protein is expressed. Format: this column is fromed by pairs of ```annotation```+```GO ID```; pairs are separated by &.
    - **UniProt**: UniProt ID.
    - **PDBs**: PDB IDs of the protein's structure. IDs are separated by &.
    - **PubMeds**: PubMed IDs of publications that appear referenced in **Description**. IDs are separated by &.
    - **Sequence**: sequence of amino-acids in the protein.
    - **Sites**: important sites in the protein sequence. Raw data, to be cleaned in the future. Different pieces of information are separated by &.


- **all_human_go.csv**: file written after cleaning GO annotations in **almost_all_human_up.csv**. Columns:
    - **UniProt**: UniProt ID.
    - **GOType**: type of Gene Ontology annotation. Three unique values: "molecular function", "subcellular location" and "biological process".
    - **GOAnnot**: Gene Ontology annotation.
    - **GOID**: Gene Ontology annotation ID. It is a string type, not integer (it is important to preserve leading zeros).

- **all_human_pdb.csv**: file written after cleaning PDB IDs in **almost_all_human_up.csv**. Columns:
    - **UniProt**: UniProt ID.
    - **PDB**: PDB ID.

- **all_human_uniprot_ids.csv**: file with 20370 UniProt IDs of human proteins with status = "reviewed". A single column with the UniProt IDs.