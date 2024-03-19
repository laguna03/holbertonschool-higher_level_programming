#!/usr/bin/python3
"""print all states that match the argument"""

import MySQLdb as sql
from sys import argv

if __name__ == '__main__':
    db = sql.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], state_name=argv[4])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{} .format(state_name)")
    rows = cur.fetchall()
    for row in rows:
        print(row)
