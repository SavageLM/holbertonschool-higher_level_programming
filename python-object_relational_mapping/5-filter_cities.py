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
    dc.execute("SELECT * FROM cities\
         JOIN states on cities.state_id = states.id ORDER BY id ASC")
    results = dc.fetchall()
    print_results = [city[2] for city in results if city[4] == sys.argv[4]]
    print(', '.join(print_results))
    dc.close()
    db.close()


if __name__ == "__main__":
    protected_filter()
