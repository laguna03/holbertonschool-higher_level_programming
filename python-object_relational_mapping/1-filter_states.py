#!/usr/bin/python3

"""Filter states with letter N"""

import MySQLdb as sql
from sys import argv

if __name__ == '__main__':
    db = sql.connect(host="localhost", port=3306, user_name=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
