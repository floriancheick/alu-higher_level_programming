#!/usr/bin/python3
"""
Module 5-filter_cities.py
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name
                FROM cities LEFT JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s ORDER BY cities.id ASC""", (argv[4], ))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
