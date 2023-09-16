#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities of that state, 
Using the database hbtn_0e_4_usa
 """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    A script that lists all cities from the database hbtn_0e_4_usa
    Your script should take 4 arguments: mysql username, mysql password and database name
    """
    if len(argv) < 5:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])


    cur = db.cursor()

    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id ASC
    """

    cur.execute(query, (state_name))

    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print([row[1])
