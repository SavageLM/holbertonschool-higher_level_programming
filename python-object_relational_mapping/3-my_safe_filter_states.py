#!/usr/bin/python3
"""This is a script for creating an SQL query from input"""

import MySQLdb
import sys


def protected_filter():
    """ turns user input into an SQL query"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
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
