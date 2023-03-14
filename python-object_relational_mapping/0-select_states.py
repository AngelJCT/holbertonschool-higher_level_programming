#!/usr/bin/python3
"""Module 0-select_states"""
import MySQLdb

def main():
    """Main function"""
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                            passwd="root", db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
