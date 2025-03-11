import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def getBin(n):
    s = bin(n)[2:]
    return '0'*(8 - len(s)) + s

x = 0
dx = 0
period_str = input ("Enter sleep period: ")
period_float = float (period_str)

try:
    while True:
        if x == 0:
            dx = 1
        elif x == 255:
            dx = -1

        GPIO.output (dac, list(map(int, getBin(x))))
        x += dx

        time.sleep (period_float)

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()