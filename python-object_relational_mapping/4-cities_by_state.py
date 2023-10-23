#!/usr/bin/python3
"""This is a script for creating an SQL query from input"""

import MySQLdb
import sys


def protected_filter():
    """ turns user input into an SQL query"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    dc = db.cursor()
    dc.execute("SELECT * FROM cities.id, cities.name, states.name FROM cities\
        INNER JOIN states on cities.state_id = states.id ORDER BY id ASC")
    results = dc.fetchall()
    for row in results:
        print(row)
    dc.close()
    db.close()


if __name__ == "__main__":
    protected_filter()
