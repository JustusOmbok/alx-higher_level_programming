#!/usr/bin/python3
"""
 a script that lists all states 
 from the database hbtn_0e_0_usa
 """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    A script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql password and database name
    """
    if len(argv) < 4:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])


    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name, FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC""")

    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
        print(row)
