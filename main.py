##built in
import sqlite3
 
##local
import extraction as ex
import numpy
import db
# from db.insert import InsertError
# import API 


import time


DB_NAME = 'coco.sqlite'
batch = 'df/df1.csv'

RESUME = False

if RESUME == False:
	### kickstart crowlar
	conn, cur = db.Setup(DB_NAME,batch)

else:
	conn, cur =db.ConnectDB(DB_NAME)



for i in range(5):
	try:
		cur.execute('SELECT coconut_id, unique_smiles FROM NP WHERE CID is 0  ORDER BY RANDOM() LIMIT 1')
		row = cur.fetchone()
		cocoid, smiles = row
		cid = ex.get_cid(smiles)
		db.insert_cid(cur, cid, cocoid)
		print(cid, smiles)
		conn.commit()
	except:
		db.insert_error(cur, cocoid)
