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

    def start():
        self.timer = time.time()

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
        with open("data_file.json", "w") as write_file:
            json.dump(self.data, write_file)

    

  

