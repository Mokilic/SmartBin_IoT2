import sqlite3 
from moduler.ultrasonisk_sensor import getHCSRdata 
from moduler.dato import dato1, dato2
from moduler.batteri import bat_funktion
import moduler.GPS

dbname = 'Gruppe3.db' 

def logdata1(a, b, c):
    conn = sqlite3.connect(dbname) 
    curs = conn.cursor() 
    curs.execute("INSERT INTO IoT2(år_måned_dag, timer_minutter, percentage) VALUES (?, ?, ?)", (a, b, c)) 

    data = (a, b, c) 
    print(f"Inserting data: {data}") 
    conn.commit() 
    conn.close() 

def logmain1(): 
    percentage = getHCSRdata() 
    år_måned_dag = dato1() 
    timer_minutter = dato2() 
    a = år_måned_dag 
    b = timer_minutter
    c = percentage
    logdata1(a, b, c)

def logdata2(a, b, c):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute("INSERT INTO gps_data(latitude, longtitude, adc_value) VALUES (?, ?, ?)", (a, b, c)) 
    data = (a, b, c)
    print(f"Inserting gps data: {data}")
    conn.commit()
    conn.close()

def logmain2():
    gps_port = "/dev/serial0" 
    ser = moduler.GPS.port_setup(gps_port) 
    gps_coords = moduler.GPS.parseGPSdata(ser) 
    adc_value = bat_funktion() 
    if gps_coords is not None: 
        a = gps_coords[0] 
        b = gps_coords[1] 
        c = adc_value 
        logdata2(a, b, c) 
    else:
        print("Failed to get GPS data.")
