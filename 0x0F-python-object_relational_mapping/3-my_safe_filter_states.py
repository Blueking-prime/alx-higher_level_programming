#!/usr/bin/python3
'''Read states from database, filtered safely, custom'''
if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=usr,
        passwd=pwd,
        db=dbname,
        port=3306
        )
    cur = db.cursor()
    cur.execute("""SELECT *
                FROM states
                WHERE name=%s
                ORDER BY id ASC""", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
