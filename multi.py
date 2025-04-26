from machine import Pin
import time

led1 = Pin(16, Pin.OUT) # green
led2 = Pin(18, Pin.OUT) # orange
led3 = Pin(17, Pin.OUT) # blue
led4 = Pin(27, Pin.OUT) # red

while True:
    led1.on()
    time.sleep_ms(100)
    led1.off()
    time.sleep_ms(100)
    led2.on()
    time.sleep_ms(100)
    led2.off()
    time.sleep_ms(100)
    led3.on()
    time.sleep_ms(100)
    led3.off()
    time.sleep_ms(100)
    led4.on()
    time.sleep_ms(100)
    led4.off()
    time.sleep_ms(100)
