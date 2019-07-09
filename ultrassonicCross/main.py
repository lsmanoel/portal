import RPi.GPIO as GPIO
import time
from Car import Car
import cross_detector as cd 

laps = input("Número de voltas: ")
carLen = input("Larguda do carro: ")
baseLen = cd.calibrate()

car1 = Car(1)
car1.start()        # inicializar no momento adequado

print("Start race!")
print("Total laps: %d"%laps)

state = False
lastState = False

try:
    while laps > 0:
        state = False
        if cd.lineCrossed(baseLen,carLen) !=0:
            state = True
            lastState = True
        elif state == False and lastState == True:
            lastState = False
            laps=laps-1
            print("Laps remaining: %d"%laps)
            car1.lapIncrement(1)

        time.sleep(0.03)
    print("Finish!!")
    GPIO.cleanup()
    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
