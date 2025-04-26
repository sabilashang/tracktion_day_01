from machine import PWM, Pin
import time

buzzer = PWM(Pin(25))  # Magicbit buzzer pin
buzzer.freq(9500)      # Set to high frequency
buzzer.duty(512)       # 50% duty cycle

time.sleep(10)          # Play for 1 second

buzzer.duty(0)         # Stop the buzzer
buzzer.deinit()
