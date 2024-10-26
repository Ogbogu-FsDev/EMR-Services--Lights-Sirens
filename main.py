from machine import Pin, PWM, Timer,I2C
import utime

# Buzzer
buzzer = PWM(Pin(15))
buzzer.duty_u16(1000)

# Button
button1 = Pin(10, Pin.IN, Pin.PULL_UP)
button2 = Pin(11, Pin.IN, Pin.PULL_UP)
button3 = Pin(12, Pin.IN, Pin.PULL_UP)

# Police LED
led1 = Pin(0, Pin.OUT) # Red
led2 = Pin(1, Pin.OUT) # Blue

# Ambulance LED
led3 = Pin(2, Pin.OUT) # Green
led4 = Pin(3, Pin.OUT) # Blue

# Fire Brigade LED
led5 = Pin(4, Pin.OUT) # Red
led6 = Pin(5, Pin.OUT) # Red

# Cancel Button
button4 = Pin(14, Pin.IN, Pin.PULL_UP)
