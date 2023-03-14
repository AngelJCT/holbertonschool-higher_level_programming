#!/usr/bin/python3
"""Module 3-my_safe_filter_states"""

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
    query = "SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    for row in cur:
        print(row)
