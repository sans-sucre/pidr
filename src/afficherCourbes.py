import csv
import numpy as np
import matplotlib.pyplot as plt

file_mes = "data_mes.csv"
file_ref = "data_ref.csv"

def afficherCourbes (nomdefichier : str) :
    ## Cette fonction affiche la courbe mettant en avant l'azimut et la hauteur dans un fichier csv donné

    file = open(nomdefichier,"r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimutList = []
    elevationList = []
    timeList = []
    for m in range (len(data[0])):
        timeList.append(m*5/60)
        azimutList.append(int(data[0][m]))
        elevationList.append(int(data[1][m]))

    plt.plot(timeList, azimutList, label = "Azimut")
    plt.plot(timeList, elevationList, label = "Hauteur")
    
    plt.xlabel('Heure de la journée')
    plt.ylabel('Degré de l\'angle')
    plt.title('Evolution de l\'azimut et la hauteur au cours d\'une journée ')
    plt.legend()
    plt.show()


afficherCourbes(file_ref)
afficherCourbes(file_mes)
