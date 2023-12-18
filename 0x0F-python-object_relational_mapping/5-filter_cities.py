#!/usr/bin/python3
"""
    Contains a script that interacts with a database
"""
import MySQLdb
import sys


def main():
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT id FROM states WHERE name like '{}'".format(sys.argv[4])
    cur.execute(sql)
    rows = cur.fetchall()
    index = rows[0][0]
    sql = "SELECT cities.name FROM cities WHERE cities.state_id = {}".format(index)
    cur.execute(sql)
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i == len(rows) - 1:
            print(rows[i][0])
        else:
            print(rows[i][0], end=", ")


if __name__ == "__main__":
    main()
