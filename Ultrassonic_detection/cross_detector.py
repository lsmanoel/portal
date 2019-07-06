import RPi.GPIO as GPIO
import time
 
GPIO_TRIGGER1 = 23
GPIO_ECHO1 = 24
GPIO_TRIGGER2 = 17
GPIO_ECHO2 = 27
SOUND_SPEED = 34300  #cm/s

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

########## Calcula a distância pelo lado direito ##########

def distance1():
    GPIO.output(GPIO_TRIGGER1, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
 
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * SOUND_SPEED) / 2
    return distance


########## Calcula a distância pelo lado esquerdo #########

def distance2():
    GPIO.output(GPIO_TRIGGER2, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
 
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * SOUND_SPEED) / 2
    return distance


######### Verifica a passagem pela linha de chegada ########

def lineCrossed(baseLen,carLen):
    dist1 = distance1()             # chama cada utrassom em sequência
    dist2 = distance2()
    checkCross1 = baseLen - dist1
    checkCross2 = baseLen - dist2
    totlen = baseLen - (checkCross1 + checkCross2)

    if distance1() < baseLen:       # passou alguma coisa
        if totLen > carLen*1.1:     # passou mais de 1 carro (carLen*1.2 -> margem para variação)
            return 2
        else:
            return 1
    else:
        return 0
 

######### Calibra a distância da base fazendo a média ########

def calibrate():
    acc = 0

    for i in range(1,10)
        acc = acc + distance1()

    return acc/i    




