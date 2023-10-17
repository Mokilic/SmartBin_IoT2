import smbus

device_address = 0x49

i2c_bus_number = 1
i2c_bus = smbus.SMBus(i2c_bus_number)

def bat_funktion():
    adc_bytes = i2c_bus.read_i2c_block_data(device_address, 0x00, 2)

    adc_value = ((adc_bytes[0] & 0b11) << 8) + adc_bytes[1]

    return adc_value