#!/usr/bin/python3
"""
Module that lists all cities by state
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                    FROM cities LEFT JOIN states
                    ON states.id = cities.state_id WHERE states.name = %s
                    ORDER BY cities.id ASC""", (argv[4],))
    rows = cur.fetchall()
    lenOf = len(rows)
    count = 1
    for row in rows:
        for col in row:
            print(col, end="")
        if (count < lenOf):
            count += 1
            print(", ", end="")
    print()
    cur.close()
    db.close()
