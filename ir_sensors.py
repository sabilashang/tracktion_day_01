from machine import Pin
import time

IR_PIN = 26
ir_sensor = Pin(IR_PIN, Pin.IN)

def read_ir_sensor():
    if ir_sensor.value() == 0:
        print(ir_sensor.value())
        return "Obstacle Detected"
    else:
        print(ir_sensor.value())
        return "No Obstacle"
    
try:
    while True:
        status = read_ir_sensor()
        print(status)
        time.sleep_ms(500)
except KeyboardInterrupt:
    print("Program Stopped")