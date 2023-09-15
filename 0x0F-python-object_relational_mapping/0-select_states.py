#!/usr/bin/python3
"""getting started with the python module MySQLdb"""

if __name__ == "__main__":
	import MySQLdb

	conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
	cur = conn.cursor()
	cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
	query_rows = cur.fetchall()
	for row in query_rows:
		print(row)
	cur.close()
	conn.close()

