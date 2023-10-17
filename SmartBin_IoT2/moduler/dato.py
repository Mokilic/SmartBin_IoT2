from datetime import datetime
import pytz  

def dato1():
    tz = pytz.timezone('Europe/Oslo') 
    now = datetime.now(tz)  
    timer_minutter = now.strftime("%H:%M")  

    return timer_minutter

def dato2():
    tz = pytz.timezone('Europe/Oslo')  
    now = datetime.now(tz) 
    år_måned_dag = now.strftime("%Y/%m/%d")  

    return år_måned_dag