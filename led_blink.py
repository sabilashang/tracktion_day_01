from machine import Pin
import random
import time

# time_values = [100,200,300,400,500,600,700,800,900]  # Renamed variable

ledcolours = ["led1", "led3"]

led1 = Pin(16, Pin.OUT) # green
led2 = Pin(18, Pin.OUT) # orange
led3 = Pin(17, Pin.OUT) # blue
led4 = Pin(27, Pin.OUT) # red

# for i in range(10):
choice = random.choice(ledcolours)

if choice == "led1":
    led1.on()
    time.sleep_ms(500)
    led1.off()
    time.sleep_ms(500)
else:
    led3.on()
    time.sleep_ms(500)
    led3.off()
    time.sleep_ms(500)
        