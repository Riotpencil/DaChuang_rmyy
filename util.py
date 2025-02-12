import pandas as pd

def get_data(name):
    # return
    filename = f"{name}.csv"
    gene_data = pd.read_csv(filename, index_col=0, sep=';')
    duplicates = gene_data.index[gene_data.index.duplicated()].unique()
    result = gene_data.loc[~gene_data.index.duplicated(keep='first')]
    return result

def exist(genes, exp):
    not_found_genes = [gene for gene in genes if gene not in exp.index]
    if not_found_genes:
        print("not found: ", len(not_found_genes))
        return False
    else:
        return True

def pick_col(genes, exp):
    if not exist(genes, exp):
        pass
    valid_index = [row for row in genes if row in exp.index]
    return exp.loc[valid_index]

def pick_row(index, genes):
    valid_index = [col for col in index if col in genes.columns]
    return genes[valid_index]

