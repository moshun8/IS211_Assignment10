#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""query pets"""

import sqlite3
import sys

con = None


try:
    con = sqlite3.connect('pets.db')
    data = con.cursor()

    pickPerson = raw_input('Please select an ID number: ')
    query = "SELECT * FROM person WHERE id =?"

    if pickPerson == '-1':
        sys.exit()
    else:
        for row in data.execute(query, [(pickPerson)]):
            print row
    # person = data.fetchone()

except sqlite3.Error as e:
    print "Closing."
    print "Error {0}".format(e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()