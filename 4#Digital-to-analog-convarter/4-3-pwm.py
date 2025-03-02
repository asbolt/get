import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setup (21, GPIO.OUT)

p = GPIO.PWM (21, 1000)
p.start(0)

try:
    while True:
        n = int (input ("Enter the fill factor: "))

        try:
            p.ChangeDutyCycle (n)
            time.sleep (10)

        except KeyboardInterrupt:
            pass

finally:
    p.stop()
    GPIO.cleanup()