#!/usr/bin/python3
'''Read cities in a state from database'''
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
    cur.execute("""SELECT name
                FROM cities
                WHERE state_id = (
                    SELECT id
                    FROM states
                    WHERE name = %s
                )
                ORDER BY id ASC;""", (state_name,))

    rows = cur.fetchall()
    check = 0
    for row in rows:
        if check == 1:
            print(', ', end='')
        for name in row:
            print(name, end='')
        check = 1
    print('')

    cur.close()
    db.close()
