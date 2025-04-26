from machine import Pin, ADC
import time


ldr = ADC(Pin(36))
ldr.atten(ADC.ATTN_11DB)
light = Pin(32, Pin.OUT)

dark_threshold = 800

while True:
    ldr_value = ldr.read()
    print("LDR Value:", ldr_value)

    if ldr_value > dark_threshold:
        light.value(1)
    else:
        light.value(0)

    time.sleep(0.5)
