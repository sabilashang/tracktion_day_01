from machine import Pin
import time

led_pin = Pin(32, Pin.OUT)

while True:
    led_pin.value(1)
    time.sleep(1)

    led_pin.value(0)
    time.sleep(1)
