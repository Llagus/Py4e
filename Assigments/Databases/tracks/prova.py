import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT id FROM Album WHERE title = "I"')
row = cur.fetchone()
print(type(row))
print(row)

conn.commit()