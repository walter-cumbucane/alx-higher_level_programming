#!/usr/bin/python3
"""
    Contains a script that interacts with a database
"""
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
sql = "SELECT * FROM states ORDER BY id ASC"
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
