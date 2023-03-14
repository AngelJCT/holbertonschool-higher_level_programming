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
        db=database,
        state=state_name
        )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '%s' ORDER BY id ASC"
    cur.execute(query, (state_name))
    for row in cur:
        print(row)
