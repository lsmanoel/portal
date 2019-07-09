# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from Car import Car
import cross_detector as cd 
import os
import sys
import cv2
import dlib


# dataset_folder_path = "./objectSense/dataset/2019-06-26/lowsize/"
# svn_path = os.path.join(dataset_folder_path, "detector.svm")
# landmarks_path = os.path.join(dataset_folder_path, "landmarks.dat")
# detector = dlib.fhog_object_detector(svn_path)
# landmarks_detector = dlib.shape_predictor(landmarks_path)
# capture = cv2.VideoCapture(0)

# Imprime a seleção do objeto =======================================

def printLandmark(image, landmarks, color):    
    # for p in landmarks.parts():
    #     cv2.circle(image, (p.x, p.y), 20, color, 2)
    pass

# Detecta a imagem ===================================================
def getImageDetect():
    # while 1:
        # ret, frame = capture.read()               # captura frame da camera

        # frame = open("./objectSense/dataset/2019-06-26/IMG_20190626_083033644.jpg")  # frame da imagem, teste
        # [boxes, confidences, detector_idxs]  = dlib.fhog_object_detector.run(detector, 
        #                                                                     frame, 
        #                                                                     upsample_num_times=1, 
        #                                                                     adjust_threshold=0.0) 
        # print("Got frame.   Conf:%0.2f      Id:%d"%(confidences,detector_idxs))                 

        # for box in boxes:
        #     e, t, d, b = (int(box.left()), 
        #                 int(box.top()), 
        #                 int(box.right()), 
        #                 int(box.bottom()))
            
        #     cv2.rectangle(frame, (e, t), (d, b), (0, 0, 255), 2)
            
        #     landmark = landmarks_detector(frame, box)
        #     printLandmark(frame, landmark, (255, 0, 0))

        # cv2.imshow("Video", frame)

        # # -------------------------------------------------
        # # Esc -> EXIT while
        # while 1:
        # k = cv2.waitKey(1) & 0xff
        # if k ==13 or k==27:
        #     break

        # if k == 27:
        #     break
        # # -------------------------------------------------
    # capture.release()
    # cv2.destroyAllWindows()
    # return confidences, detector_idxs
    return [0.8, 2] #debug

# Inicializa todos os competidores ==========================
def loginCars():
    competidors = []
    competidors.append(Car(1))
    competidors.append(Car(2))
    competidors.append(Car(3))

    # i = 'c'                                               # para fazer interativamente
    # id = input('Entre com id do competidor: ')
    # competidors.append(Car(id))
    # while i != 'n':
    #     id = input('Entre com id do competidor: ')
    #     competidors.append(Car(id))
    #     i = input('Registar outro competidor? (s/n): ')
    
    return competidors

# Inicializa os timers dos carros ===========================
def startCars(cars):
    for car in cars:
        car.start()    
  
# Atualiza o status a cada volta ============================
#  -Verificar os tempos de cada competidor para atribuir sua posição
#  -Verificar se a passagem foi a do que está em primeiro, para aí decrementar o total de voltas
def raceStatus(cars,laps,conf,detId):
    # if conf > 0.8:
    #     for car in cars:
    #         if cars[detId].lapsTimes[laps] < car.lapsTimes[laps]:
    #             cars[detId].lapIncrement(1)
    #         else:
    #             cars[detId].lapIncrement(2)
    # incompleto ....

    # para testes com 1 carro
    cars[0].lapIncrement(1)
    buzzer(1)
    return laps-1

# Buzzer para os eventos ====================================
def buzzer(state):
    # 0 => inicia a corrida     longo
    # 1 => passagem pela linha  curto
    # 2 => fim da corrida       3 pulsos
    pass

############################################################# 
# Inicia o programa =========================================
laps = 1
laps = int(input("Número de voltas: "))
# carLen = input("Larguda do carro: ")
cars = loginCars()
baseLen = cd.calibrate()-1
start = input("Aperte enter para iniciar a corrida... ")
startCars(cars)
buzzer(0)
conf = 0
detId = 0

try:
    while laps > 0:
        state = False
        if cd.lineCrossed(baseLen,carLen) !=0:            # está medindo a passagem
            [conf,detId] = getImageDetect()               # chama a captura de video, (poderia ser em multithread)
            state = True
            lastState = True
        elif state == False and lastState == True:        # terminou de medir a passagem
            lastState = False
            print("Voltas faltando: %d"%laps)
            laps = raceStatus(cars,laps,conf,detId)       # atualiza o status da corrida    
        time.sleep(0.03)    
    print("Finish!!")
    buzzer(2)
    GPIO.cleanup()                                        # limpa o buffer do gpio
# Reset CTRL + C
except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
    GPIO.cleanup()
