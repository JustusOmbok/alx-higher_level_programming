#!/usr/bin/python3
"""
 a script that lists all states 
 from the database hbtn_0e_0_usa
 """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Accesses database 
    and gets states from database
    """
    if len(argv) < 5:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])


    cur = db.cursor()

    query = "SELECT * FROM states \
            WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC"

    cur.execute(query, {'name': (argv[4])})

    rows = cur.fetchall()

    for row in rows:
        print(row)
