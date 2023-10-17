import serial 
import pynmea2 
from time import sleep

def port_setup(port):
    ser = serial.Serial(port, baudrate=9600, timeout=2)
    return ser

def parseGPSdata(ser):
        keywords = ["$GPRMC","$GPGGA"]
        gps_data = ser.readline() 
        try:
            gps_data = gps_data.decode("utf-8") 
        except UnicodeDecodeError:
            return None 


        if len(gps_data) > 5: 
            if gps_data[0:6] in keywords: 
                gps_msg = pynmea2.parse(gps_data) 
                lat = gps_msg.latitude
                lng = gps_msg.longitude
                return (lat,lng)
            else:
                return None 
        else:
            return None

if __name__ == "__main__":

    gps_port = "/dev/serial0" 
    ser = port_setup(gps_port)

    print("GPS coordinate Stream:")
    while True:
        try:
            gps_coords = parseGPSdata(ser) 
            if gps_coords is None or gps_coords[0] == 0.0: 
                print("No Data")
            else:
                print(f"latitude: {gps_coords[0]}, longitude: {gps_coords[1]}") 
            sleep(5)

        except serial.SerialException as e:
            print(f"\nERROR: {e}")
            print("... reconnecting to serial\n")
            ser = port_setup()

        except KeyboardInterrupt as e: 
            print("--- Program shutting down ---")
            break