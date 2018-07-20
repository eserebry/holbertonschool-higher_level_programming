#!/usr/bin/python3


def list_states():
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    result = cur.fetchall()
    for row in result:
        print(row)
    db.close()

if __name__ == "__main__":
    import MySQLdb
    import sys
    list_states()
