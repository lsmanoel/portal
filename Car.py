import time
import json

class Car:
    def __init__(self,id):
        self.id = id
        self.laps = 0
        self.lapsTimes = []
        self.timer = 0
        self.position = []
        self.data = {"id":"","lap":"","position":"","lap_times":""}
        self.data["id"] = id

    def start(self):
        self.timer = time.time()
        print("Car%d started!"%self.id)

    def lapIncrement(self,position):
        timeCounter =  time.time() - self.timer 
        self.lapsTimes.append(timeCounter)
        self.timer = time.time()
        self.position.append(position)
        self.laps = self.laps + 1
        self.data["lap"] = self.laps
        self.data["position"] = position
        self.data["lap_times"] = self.lapsTimes
        
        # para enviar o arquivo por mqtt
        file = "car"+str(self.id)+"_data_file.json"
        with open(file, "w") as write_file:
            json.dump(self.data, write_file)
        # print("Car%d Times: "%self.id)
        # print(self.data["lap_times"])

    

  

