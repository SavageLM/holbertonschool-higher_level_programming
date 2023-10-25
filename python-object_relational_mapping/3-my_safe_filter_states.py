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
    dc.execute("SELECT * FROM states WHERE name = %(user_input)s\
        ORDER BY id ASC", {'user_input': sys.argv[4]})
    results = dc.fetchall()
    for state in results:
        print(state)
    dc.close()
    db.close()


if __name__ == "__main__":
    protected_filter()
