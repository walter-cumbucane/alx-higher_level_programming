#!/usr/bin/python3
"""
    Queries data from a database using a native sql driver
"""
from sys import argv
import MySQLdb


def main():
    """
        Main Function
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(host="localhost",
                           user=username,
                           passwd=password,
                           db=database
                           )
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
