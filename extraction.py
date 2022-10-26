import requests as req
def get_cid(smiles):

    pload= {'smiles':smiles}
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/cids/txt'
    r = req.post(url, data=pload)
    return r.text

    