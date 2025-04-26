from machine import Pin, PWM
import time

TRIG_PIN = 12
ECHO_PIN = 14

BUZZER_PIN = 25
buzzer = PWM(Pin(BUZZER_PIN), freq=1000, duty=512)

trigger = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


def get_distance():
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    start_time = time.ticks_us()

    while echo.value() == 0:
        start_time = time.ticks_us()

    while echo.value() == 1:
        end_time = time.ticks_us()

    pulse_duration = time.ticks_diff(end_time, start_time)

    # Calculate distance (speed of sound = 343 m/s)
    distance = (pulse_duration * 0.0343) / 2  # Distance in cm
    return distance


def ring_buzzer():
    buzzer.duty(512)
    time.sleep(1)
    buzzer.duty(0)


try:
    while True:
        distance = get_distance()
        print("Distance: {:.2f} cm".format(distance))

        if distance < 40:
            print("Someone is near, ringing the doorbell!")
            ring_buzzer()
        else:
            print("No one detected.")

        time.sleep(1)

except KeyboardInterrupt:
    print("Program Stopped")
