# Buzzer

from machine import Pin, PWM
import time

BUZZER_PIN = 25
buzzer = PWM(Pin(BUZZER_PIN))

def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty(512)
    time.sleep_ms(duration)
    bizzer.duty(0)
    
def stop_buzzer():
    buzzer.duty(0)

try:
    while True:
        play_tone(261,500)
        time.sleep_ms(100)
        play_tone(293,500)
        time.sleep_ms(100)
        play_tone(323,500)
        time.sleep_ms(100)
        play_tone(343,500)
        time.sleep_ms(100)
        play_tone(392,500)
        time.sleep_ms(100)
        
except KeyboardInterrupt:
    stop_buzzer()
    buzzer.deinit()
        