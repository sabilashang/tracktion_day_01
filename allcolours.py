from machine import Pin
import time

led1 = Pin(16, Pin.OUT)  # green
led2 = Pin(18, Pin.OUT)  # orange
led3 = Pin(17, Pin.OUT)  # blue
led4 = Pin(27, Pin.OUT)  # red

while True:
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    time.sleep(1)
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    time.sleep(1)
