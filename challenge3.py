from machine import Pin, ADC
import time

IR_PIN = 26

# Setup
ir_sensor = ADC(Pin(IR_PIN), atten=ADC.ATTN_11DB)

# Threshold for classifying black vs white (adjust as needed)
threshold = 2000  

def read_ir_sensor():
    ir_sensor_value = ir_sensor.read()
    return ir_sensor_value

def scan_boxes():
    black_count = 0
    white_count = 0
    
    # Loop over 4 boxes
    for i in range(1, 5):  # Box 1 to 4
        print(f"Scanning Box {i}...")
        status = read_ir_sensor()
        print(f"Box {i} IR Sensor Status: {status}")

        if status < threshold:  # Black box (lower IR value)
            black_count += 1
        else:  # White box (higher IR value)
            white_count += 1
        
        # Optional: Add a small delay between scans
        time.sleep(1)
    
    print(f"Total Black Boxes: {black_count}")
    print(f"Total White Boxes: {white_count}")

# Main loop
while True:
    scan_boxes()  # Scan the boxes and count
    time.sleep(3)  # Delay before scanning again (optional)
