import sqlite3 as lite
import sys
con = lite.connect('Gruppe3.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS IoT2")
    cur.execute("DROP TABLE IF EXISTS gps_data")
    cur.execute("CREATE TABLE IoT2(id INTEGER PRIMARY KEY AUTOINCREMENT, år_måned_dag DATETIME, timer_minutter TIMESTAMP, percentage NUMERIC)")
    cur.execute("CREATE TABLE gps_data(id INTEGER PRIMARY KEY AUTOINCREMENT, latitude FLOAT, longtitude FLOAT, adc_value INTEGER)")

