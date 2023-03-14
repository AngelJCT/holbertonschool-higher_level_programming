#!/usr/bin/python3
"""Module 2-my_filter_states"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    cur = db.cursor()
    query = f"SELECT * FROM states WHERE name LIKE '{state_name}' ORDER BY id ASC"
    cur.execute(query, (state_name,))
    for row in cur:
        print(row)
