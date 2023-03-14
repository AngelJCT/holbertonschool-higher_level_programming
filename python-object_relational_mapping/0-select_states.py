#!/usr/bin/python3
"""Module 0-select_states"""
import MySQLdb


def connect_to_db():
    """Main function"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        db="hbtn_0e_0_usa"
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur:
        print(row)


if __name__ == "__main__":
    connect_to_db()
