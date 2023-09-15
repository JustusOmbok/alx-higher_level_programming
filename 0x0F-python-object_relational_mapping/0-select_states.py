#!/usr/bin/python3
"""
 a script that lists all states from the database hbtn_0e_0_usa
 """
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Accesses database and gets states from database
    """
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <myaql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    databse_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )


    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


    cursor.close()
    db.close()
