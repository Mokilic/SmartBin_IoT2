from flask import Flask, render_template  
import sqlite3  

import time  
app = Flask(__name__)  


def getData():  
    conn = sqlite3.connect('../Gruppe3.db')  
    curs = conn.cursor()  


    for row in curs.execute("SELECT * FROM IoT2 ORDER BY id DESC LIMIT 1"):  
        år_måned_dag = str(row[1])  
        timer_minutter = str(row[2])  
        percentage = row[3]  
    
    for row in curs.execute("SELECT * FROM gps_data ORDER BY id DESC LIMIT 1"):  
        latitude = row[1]  
        longtitude = row[2]  
        adc_value = row[3]  
    conn.close()  
    return timer_minutter, år_måned_dag, percentage, latitude, longtitude, adc_value  

@app.route('/')  
def index():  
  år_måned_dag, timer_minutter, percentage, latitude, longtitude, adc_value = getData()  
  templateData = {  
    'timer_minutter': timer_minutter,
    'år_måned_dag': år_måned_dag,
    'percentage': percentage,
    'latitude': latitude,
    'longtitude': longtitude,
    'adc_value': adc_value
  }
  return render_template('index.html', **templateData)  

if __name__ == '__main__': 
  app.run(debug=True) 
