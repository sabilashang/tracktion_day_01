from machine import Pin, ADC
import time

IR_PIN = 26

ir_Sensor = ADC(Pin(IR_PIN), atten = ADC.ATTN_11DB)

def read_ir_sensor():
    ir_sensor_value = ir_Sensor.read()
    return ir_sensor_value


try:
    while True:
        status = read_ir_sensor()
        print(status)
        time.sleep_ms(500)
        
except KeyboardInterrupt:
    print("Program stopped")