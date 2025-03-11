import RPi.GPIO as GPIO
import time
 
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
 
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)
 
def getBin(n):
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s
 
def adc():
    x = 0
 
    x += 128
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 128
    
    x += 64
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 64
    
    x += 32
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 32
    
    x += 16
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 16
    
    x += 8
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 8
    
    x += 4
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 4
    
    x += 2
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 2
    
    x += 1
    list_value = list(map(int, getBin(x)))
    GPIO.output(dac, list_value)
    time.sleep(0.01)
    if GPIO.input(comp) == GPIO.HIGH:
        x -= 1

    return x
    
try:
    while True:
        i = adc()
        value = i * 3.3 / 256.0
        if i:
            print (f"{i}")
            print (f"{value:.2} volt")
    
finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()