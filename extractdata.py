import sqlite3
import csv

query = """
DROP TABLE IF EXISTS restaurants;
CREATE TABLE restaurants
( 'camis' varchar(200)
, 'dba' varchar(200)
, 'boro' varchar(200)
, 'building' varchar(200)
, 'street' varchar(200)
, 'zipcode' varchar(200)
, 'phone' varchar(200)
, 'cuisine description' varchar(200)
, 'inspection date' varchar(200)
, 'action' varchar(200)
, 'violation code' varchar(200)
, 'violation description' varchar(200)
, 'critical flag' varchar(200)
, 'score' varchar(200)
, 'grade' varchar(200)
, 'grade date' varchar(200)
, 'record date' varchar(200)
, 'inspection type' varchar(200)
);

"""

con = sqlite3.connect(':memory')
cursor = con.cursor()
cursor.executescript(query)

with open('Restaurant_Inspection_Results.csv','rb') as filx:
    dr = csv.DictReader(filx) # comma is default delimiter
    to_db = [(i['CAMIS'].decode('utf8'), i['DBA'].decode('utf8'), i['BORO'].decode('utf8'), i['BUILDING'].decode('utf8'), i['STREET'].decode('utf8'), i['ZIPCODE'].decode('utf8'), i['PHONE'].decode('utf8'), i['CUISINE DESCRIPTION'].decode('utf8'), i['INSPECTION DATE'].decode('utf8'), i['ACTION'].decode('utf8'), i['VIOLATION CODE'].decode('utf8'), i['VIOLATION DESCRIPTION'].decode('utf8'), i['CRITICAL FLAG'].decode('utf8'), i['SCORE'].decode('utf8'), i['GRADE'].decode('utf8'), i['GRADE DATE'].decode('utf8'), i['RECORD DATE'].decode('utf8'), i['INSPECTION TYPE'].decode('utf8')) for i in dr]

try:
	cursor.executemany("INSERT INTO restaurants values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
	con.commit()
	con.close()

except sqlite3.Error as er:
	print("something went wrong " + er)




