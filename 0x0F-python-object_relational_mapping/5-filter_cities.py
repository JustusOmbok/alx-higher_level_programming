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

    query = "SELECT cities.id, cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s \
            ORDER BY cities.id ASC"

    cur.execute(query, {'states_name': argv[4]})

    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(",".join([row[1]]))
