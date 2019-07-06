import RPi.GPIO as GPIO
import time

laps = input("Número de voltas: ")
carLen = input("Larguda do carro: ")
baseLen = calibrate()

car1 = Car(1)
car1.start()        # inicializar no momento adequado

print("Start race!")
print("Total laps: %d"%laps)

state = False
lastState = False

try:
    while laps > 0:
        state = False
        if lineCrossed(baseLen,carLen) !=0:
            state = True
            lastState = True
        elif state == False and lastState == True:
            lastState = False
            laps=laps-1
            print("Laps remaining: %d"%laps)

        time.sleep(0.03)
    print("Finish!!")

    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
