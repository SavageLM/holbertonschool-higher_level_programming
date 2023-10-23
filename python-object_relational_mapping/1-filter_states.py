#!/usr/bin/python3
"""This is a script for listing all states in a database, hbtn_0e_usa"""

import MySQLdb
import sys


def filter_states():
    """ Finds a nd prints all states from database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    dc = db.cursor()
    dc.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
        ORDER BY id ASC")
    results = dc.fetchall()
    for state in results:
        print(state)
    dc.close()
    db.close()


if __name__ == "__main__":
    filter_states()
