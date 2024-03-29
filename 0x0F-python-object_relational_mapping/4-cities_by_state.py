#!/usr/bin/python3
"""getting started with the python module MySQLdb"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT citie.id, citie.name, state.name FROM states AS state \
    JOIN cities AS citie ON citie.state_id = state.id \
    ORDER BY citie.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
