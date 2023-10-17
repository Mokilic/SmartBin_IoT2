import RPi.GPIO as GPIO

def setup_led(red_pin, green_pin, blue_pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    GPIO.setup(red_pin, GPIO.OUT) 
    GPIO.setup(green_pin, GPIO.OUT)
    GPIO.setup(blue_pin, GPIO.OUT)
    red_pwm = GPIO.PWM(red_pin, 100) 
    green_pwm = GPIO.PWM(green_pin, 100)
    blue_pwm = GPIO.PWM(blue_pin, 100)

    red_pwm.start(0) 
    green_pwm.start(0)
    blue_pwm.start(0)

    def set_color(red, green, blue): 
        red_pwm.ChangeDutyCycle(red) 
        green_pwm.ChangeDutyCycle(green)
        blue_pwm.ChangeDutyCycle(blue)
    
    return set_color