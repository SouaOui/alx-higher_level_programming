#!/usr/bin/python3
"""getting started with the python module MySQLdb"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute(""" SELECT c.name FROM cities AS c
                    JOIN states AS s
                    ON c.state_id=s.id
                    WHERE s.name=%s
                    ORDER BY c.id ASC""", (sys.argv[4], ))
    cities = cur.fetchall()
    for i, city in enumerate(cities):
        if i == len(cities)-1:
            print(city[0])
        else:
            print(city[0], end=", ")
    # SIMO print(', '.join(tuple(city[0] for city in cities)))
    cur.close()
    conn.close()
