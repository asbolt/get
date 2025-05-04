import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=0)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    elem = 128
    t = 0.01
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 64
    else:
        elem = elem + 64
    
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 32
    else:
        elem = elem + 32
    
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 16
    else:
        elem = elem + 16
    
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 8
    else:
        elem = elem + 8
        
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 4
    else:
        elem = elem + 4
        
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 2
    else:
        elem = elem + 2
        
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 1
    else:
        elem = elem + 1

    return elem


print("до try")

try:
    meas_data = []
    start_time = time.time()
    decod = 0

    print("до 1")

    GPIO.output(troyka, 1)      #зарядка кондера
    while (decod <= 206):
        decod = adc()
        print(decod)
        meas_data.append(decod)     # добавление новых данных в лист 
 
    print("до 0")

    GPIO.output(troyka, 0)      #разрядка кондера
    while (decod >= 178):
        decod = adc()
        print(decod)
        meas_data.append(decod)     # добавление новых данных в лист  

    print("до time")

    end_time = time.time()
    experiment_time = end_time - start_time     # продолжительность эксперимента

    print("до grafic")

    plt.plot(meas_data)     #график
    plt.show()

    print("до txt")

    meas_data_str = [str(item) for item in meas_data]

    with open("data.txt", "w") as outfile:                 #сохраняем значения data в data.txt
        outfile.write("\n".join(meas_data_str))


    #set = []

    frequency = str(len(meas_data)/experiment_time)
    step = str(3.3 / 256)
    intfr = len(meas_data)/experiment_time
    period = 1 / intfr

    with open("nsettings.txt", "w") as f:
        f.write(frequency)
        f.write("\n")
        f.write(step)

    print(experiment_time, period, float(frequency), float(step))


finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
