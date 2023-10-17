import RPi.GPIO as GPIO 
import time

låg_status = "lukket" 

def getHCSRdata():
    GPIO_TRIGGER = 23  
    GPIO_ECHO = 24  
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT) 
    GPIO.setup(GPIO_ECHO, GPIO.IN) 
    GPIO.output(GPIO_TRIGGER, True) 
    GPIO.output(GPIO_TRIGGER, False)  
    StartTime = time.time()  
    StopTime = time.time()
      
    while GPIO.input(GPIO_ECHO) == 0:  
        StartTime = time.time()  
    while GPIO.input(GPIO_ECHO) == 1:  
        StopTime = time.time()  
    TimeElapsed = StopTime - StartTime  
    distance = round((TimeElapsed * 34300) / 2, 1)  
    percentage = round((50 - distance) / 0.5)  

    if percentage < 0:  
        percentage = 0  
    elif percentage > 100:  
        percentage = 100  

    return percentage  
