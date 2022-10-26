import sqlite3
import pandas as pd

def ConnectDB(file):
    #Creating Database and tables
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    return conn, cur


def Setup(file, batch):
    #Creating Database and tables
    conn = sqlite3.connect(file)

    cols = ['coconut_id', 'unique_smiles']
    df = pd.read_csv(batch)
    df=df[cols]
    df['CID'] = 0

    conn = sqlite3.connect(file) 
    df.to_sql('NP', conn, if_exists='replace', index=False) 

    cur = conn.cursor()

    return conn, cur


def insert_cid(cur, cid, cocoid):
    cur.execute('UPDATE NP SET CID=? WHERE coconut_id=?', (cid, cocoid) )

def insert_error(cur, cocoid):
    cur.execute('UPDATE NP SET CID=? WHERE coconut_id=?', (99999999, cocoid) )