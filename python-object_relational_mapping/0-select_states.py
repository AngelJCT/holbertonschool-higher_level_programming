#!/usr/bin/python3
"""Module 0-select_states"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main function"""
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur:
        print(row)
