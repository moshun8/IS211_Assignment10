#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""load pets"""

import sqlite3
import sys

con = None

try:
    con = sqlite3.connect('pets.db')
    data = con.cursor()

    data.execute("INSERT INTO person VALUES(1, 'James', 'Smith', 41)")
    data.execute("INSERT INTO person VALUES(2, 'Diana', 'Greene', 23)")
    data.execute("INSERT INTO person VALUES(3, 'Sara', 'White', 27)")
    data.execute("INSERT INTO person VALUES(4, 'William', 'Gibson', 23)")
    data.execute("INSERT INTO pet VALUES(1, 'Rusty', 'Dalmation', 4, 1)")
    data.execute("INSERT INTO pet VALUES(2, 'Bella', 'Alaskan Malamute', 3, 0)")
    data.execute("INSERT INTO pet VALUES(3, 'Max', 'Cocker Spaniel', 1, 0)")
    data.execute("INSERT INTO pet VALUES(4, 'Rocky', 'Beagle', 7, 0)")
    data.execute("INSERT INTO pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0)")
    data.execute("INSERT INTO pet VALUES(6, 'Spot', 'Bloodhound', 2, 1)")
    data.execute("INSERT INTO person_pet VALUES(1, 1)")
    data.execute("INSERT INTO person_pet VALUES(1, 2)")
    data.execute("INSERT INTO person_pet VALUES(2, 3)")
    data.execute("INSERT INTO person_pet VALUES(2, 4)")
    data.execute("INSERT INTO person_pet VALUES(3, 5)")
    data.execute("INSERT INTO person_pet VALUES(4, 6)")

except sqlite3.Error, e:
    print "Error {0}".format(e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()