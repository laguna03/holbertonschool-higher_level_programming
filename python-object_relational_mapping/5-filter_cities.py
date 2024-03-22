#!/usr/bin/python3

"""
This script lists all cities of a state given as parameter
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    username, password, database_name, state_name = sys.argv[1:]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    cur.execute("""
        SELECT cities.name
        FROM cities
        LEFT JOIN states
        ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id
    """, (state_name,))

    rows = cur.fetchall()
    data = [elem for row in rows for elem in row]

    print(*data, sep=', ')
