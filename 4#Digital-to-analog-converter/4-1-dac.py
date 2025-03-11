import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def getBin(n):
    s = bin(n)[2:]
    return '0'*(8 - len(s)) + s

try:
    while True:
        s = input ("Give a number from 0 to 255: ")

        try:
            n = int(s)

            if (n < 0):
                print ("Enter a number greater than 0")
                continue

            elif (n > 255):
                print ("Enter a number less than 255")
                continue

            voltage = float(n)/256.0 * 3.3
            print (f"Estimated voltage value: {voltage:.4} volt")
            GPIO.output (dac, list(map(int, getBin(n))))
        
        except ValueError:
            if s == 'q': break

            try:
                n = float(s)
                print ("Enter an integer")

            except ValueError:
                print ("Enter a number")

finally:
    GPIO.output (dac, [0]*len(dac))
    GPIO.cleanup()