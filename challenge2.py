from machine import Pin, ADC, PWM
import time

IR_PIN = 26
BUZZER_PIN = 25

# Setup
buzzer = PWM(Pin(BUZZER_PIN))
buzzer.freq(1000)  # Set buzzer frequency to 1kHz

ir_sensor = ADC(Pin(IR_PIN), atten=ADC.ATTN_11DB)

def read_ir_sensor():
    ir_sensor_value = ir_sensor.read()
    return ir_sensor_value

def black(duration=0.3):
    buzzer.duty(512)
    time.sleep(duration)
    buzzer.duty(0)

def white(duration=1):
    buzzer.duty(512)
    time.sleep(duration)
    buzzer.duty(0)

def silence(duration=0.5):
    buzzer.duty(0)  # Ensure buzzer is OFF during silence
    time.sleep(duration)

while True:
    status = read_ir_sensor()
    print("IR Sensor Status:", status)

    # Check for different sensor value ranges
    if 500 < status < 2000:
        black()  # Short "S" beep
    elif status < 100:
        white()  # Long "O" beep
    elif status > 3000:
        silence()  # No sound if value > 3000
