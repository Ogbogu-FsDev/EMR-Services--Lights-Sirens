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

def PoliceCar():
    # Red
    utime.sleep_ms(100)
    led1.value(1)
    utime.sleep_ms(100)
    led1.value(0)
    # Blue
    utime.sleep_ms(50)
    led2.value(1)
    utime.sleep_ms(50)
    led2.value(0)
    
    def Siren1():
        buzzer.freq(750)
        utime.sleep_ms(230)
        buzzer.freq(1550)
        utime.sleep_ms(100)
    Siren1()

def AmbulanceVan():
    # Green
    utime.sleep_ms(100)
    led3.value(1)
    utime.sleep_ms(100)
    led3.value(0)
    
    # Blue
    utime.sleep_ms(100)
    led4.value(1)
    utime.sleep_ms(400)
    led4.value(0)
    
    def Siren2():
        buzzer.freq(2500)
        utime.sleep_ms(100)
        buzzer.freq(2100)
        utime.sleep_ms(300)
        buzzer.freq(1700)
        utime.sleep_ms(100)
        buzzer.freq(800)
        utime.sleep_ms(100)
    Siren2()

def FireEngine():
    # Red
    utime.sleep_ms(100)
    led5.value(1)
    utime.sleep_ms(100)
    led5.value(0)
    # Red
    led6.value(1)
    
    def Siren3():
        buzzer.freq(750)
        utime.sleep_ms(100)
        buzzer.freq(1500)
        utime.sleep_ms(150)
        buzzer.freq(3500)
        utime.sleep_ms(50)
    Siren3()

# Clear function to reset the compents within a loop
def clear():
    buzzer.deinit()
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)

if __name__ == '__main__':
    while True:
        if button1.value() == 0:
            while True:
                PoliceCar()
                if button4.value() == 0:
                    break
        elif button2.value() == 0:
            while True:
                AmbulanceVan()
                if button4.value() == 0:
                    break
        elif button3.value() == 0:
            while True:
                FireEngine()
                if button4.value() == 0:
                    break
        else:
            clear()
