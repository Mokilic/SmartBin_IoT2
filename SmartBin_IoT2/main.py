from moduler.ultrasonisk_sensor import getHCSRdata 
from moduler.imu_accelerometer import imu
from moduler.rgb_led import setup_led
from moduler.logger import logmain1, logmain2
import moduler.GPS
import RPi.GPIO as GPIO
import time

def my_function():
    return None 

gps_port = "/dev/serial0" 
ser = moduler.GPS.port_setup(gps_port) 
  
set_color = setup_led(13, 19, 12) 

flag = True 
try:
    while True: 
        x = imu()[0]
        y = imu()[1]
        z = imu()[2]
        if y < 3 and z < -6 and flag: 
            låg_status = "lukket" 
            print(låg_status) 
            time.sleep(3)
            percentage = (getHCSRdata()) 
            print(f"{percentage} %") 
            logmain1() 
            flag = False 
        elif y >= 3 or z >= -8 and flag: 
            flag = True 
            låg_status = "åbent" 
            my_function() 
            print(låg_status) 
        
        if låg_status == "lukket" and percentage >= 90: 
            set_color(0, 100, 100) #Rød
        elif låg_status == "lukket" and percentage < 90 and percentage >= 30:
            set_color(0, 30, 100) #Gul
        elif låg_status == "lukket" and percentage < 60:
            set_color(100, 0, 100) #Grøn

        time.sleep(0.5)

        if int(time.time()) % 60 == 0: 
            gps_coords = moduler.GPS.parseGPSdata(ser) 
            if gps_coords is None: 
                print("No GPS data received.")
            else:
                print(f"latitude: {gps_coords[0]}, longitude: {gps_coords[1]}")
                logmain2() 

except KeyboardInterrupt: 
        GPIO.cleanup()
