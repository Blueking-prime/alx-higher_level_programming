#!/usr/bin/python3
'''Read states from database'''
if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=usr,
        passwd=pwd,
        db=dbname,
        port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
