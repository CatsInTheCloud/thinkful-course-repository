# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:32:53 2015

@author: Cat
"""

import sqlite3 as lite
con = lite.connect('getting_started.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print('SQLite version: %s' % data)

# Where do I define the cities relative to the code that drops the first data bases and then makes new ones?
   
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS <cities>")
    cur.execute("DROP TABLE IF EXISTS <weather>")

cities = (('New York City', 'NY'),
          ('Boston', 'MA'),
            ('Chicago', 'IL'),
            ('Miami', 'FL'),
            ('Dallas', 'TX'),
            ('Seattle', 'WA'),
            ('Portland', 'OR'),
            ('San Francisco', 'CA'),
            ('Los Angeles', 'CA'),
            ('Las Vegas', 'NV'),
            ('Atlanta', 'GA'))

weather = (('New York City', 2013, 'July', 'January', 62),
           ('Boston', 2013, 'July', 'January', 59),
            ('Chicago', 2013, 'July', 'January', 59),
            ('Miami', 2013, 'August', 'January', 84),  
            ('Dallas', 2013, 'July', 'January', 77),
            ('Seattle', 2013, 'July', 'January', 61),
            ('Portland', 2013, 'July', 'December', 63),
            ('San Francisco', 2013, 'September', 'December', 64),
            ('Los Angeles', 2013, 'September', 'December', 75),
            ('Las Vegas', 2013, 'July', 'December', 100), 
           ('Atlanta', 2013, 'July', 'January', 99))  
           
with con:    
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    
 # Do I need to import sqlite again?    
import pandas as pd

con = lite.connect('getting_started.db')

with con:
    
    cur = con.cursor()
    cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city")
    
    rows= cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    
    for row in rows:
        print(row)
        