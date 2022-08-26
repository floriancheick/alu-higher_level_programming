#!/usr/bin/python3
"""
Module 0-select_states.py
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    c = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cu = conn.cursor()
    cu.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cu.fetchall()
    for row in query_rows:
        print(row)
    cu.close()
    c.close()
