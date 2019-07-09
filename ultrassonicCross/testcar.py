import time
from Car import Car

laps = input("Número de voltas: ")

car1 = Car(1)
print("Id:%d"%car1.id)

start = time.time()
car1.start()
time.sleep(1.55986)
car1.lapIncrement(1)
time.sleep(1.221)
car1.lapIncrement(1)
time.sleep(1.789898)
car1.lapIncrement(1)