#!/usr/bin/python3
'''Read cities from database'''
import MySQLdb
import sys

usr = sys.argv[1]
pwd = sys.argv[2]
dbname = sys.argv[3]

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=usr,
        passwd=pwd,
        db=dbname,
        port=3306
        )
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
