#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities of that state using the database hbtn_0e_4_usa
 """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    A script that acceses the db and retrieves cities of a state
    """
    if len(argv) < 5:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])


    cur = db.cursor()

    cur.execute(query, (state_name))

    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(",".join([row[1]]))
