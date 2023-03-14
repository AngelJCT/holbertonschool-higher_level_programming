#!/usr/bin/python3
"""Module 5-filter_cities"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Lists all cities from database hbtn_0e_4_usa"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    cur = db.cursor()
    query = "SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
