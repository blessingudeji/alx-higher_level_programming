#!/usr/bin/python3
"""
Takes in argument and displays values
in the states table of hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    sql = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    sql_s = sql.cursor()
    sql_s.execute(
            "SELECT * FROM states WHERE name LIKE"
            " '{:s}' ORDER BY id ASC".format(argv[4]))
    db = sql_s.fetchall()
    for states in db:
        if states[1] == argv[4]:
            print(states)
