from mpu6050 import mpu6050

def imu():
    sensor = mpu6050(0x68) 
    accel_data = sensor.get_accel_data() 

    x = int(accel_data['x']) 
    y = int(accel_data['y'])
    z = int(accel_data['z'])

    return x, y, z 
