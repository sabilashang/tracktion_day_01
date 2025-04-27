from machine import Pin, ADC
import time
from obocar import OBOCar

# ——— Configuration ———
speed         = 512
ir_threshold  = 300              # <300=black, ≥300=white
no_of_ir_pins = 6
ir_pin_nos    = [12, 14, 27, 26, 25, 33]

# ——— Initialization ———
car           = OBOCar()
ir_sensors    = [ADC(Pin(pin), atten=ADC.ATTN_11DB) for pin in ir_pin_nos]
ir_raw_values = [0]*no_of_ir_pins

# ——— Helpers ———
def announce(msg):
    """Clear the display and show msg at top-left."""
    car.display(msg, 0, 0)

def read_sensors():
    """Read raw IR values; return booleans True=black, False=white."""
    for i in range(no_of_ir_pins):
        ir_raw_values[i] = ir_sensors[i].read()
    return [val < ir_threshold for val in ir_raw_values]

def stop():
    announce("Stop")
    car.left_motor_forward(0)
    car.right_motor_forward(0)

# ——— Main Loop ———
while True:
    sensors = read_sensors()
    # sensors = [Leftmost, Left, Mid-Left, Mid-Right, Right, Rightmost]
    leftmost, left, midL, midR, right, rightmost = sensors

    # 1) All white → No track
    if not any(sensors):
        announce("No track")
        car.stop()
        time.sleep(0.1)
        continue

    # 2) Only middle two black → Forward
    if midL and midR and not (left or right or leftmost or rightmost):
        announce("Forward")
        car.left_motor_forward(speed)
        car.right_motor_forward(speed)
        time.sleep(0.1)
        continue

    # 3) Otherwise → Stop (you can expand for turns, etc.)
    stop()
    time.sleep(0.1)

