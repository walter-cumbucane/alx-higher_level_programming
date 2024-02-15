#!/usr/bin/python3
from sys import argv
import MySQLdb


username = argv[1]
password = argv[2]
database = argv[3]

conn = MySQLdb.connect(host="localhost",
                        user=username,
                        passwd=password,
                        db=database
                       )
cur = conn.cursor()
sql = "SELECT * FROM States ORDER BY id ASC"
cur.execute(sql)
rows = cur.fetchall()
