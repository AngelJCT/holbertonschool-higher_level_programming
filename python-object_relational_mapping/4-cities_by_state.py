#!/usr/bin/python3
"""Module 4-cities_by_state"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Lists all cities from database hbtn_0e_4_usa"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cur.execute(query)
    for row in cur:
        print(row)
