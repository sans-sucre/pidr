import csv
import numpy as np
import matplotlib.pyplot as plt

file_mes = "data_mes.csv"
file_ref = "data_ref.csv"

import numpy as np

def coordonnes_polaire(x: float, y: float) :
    """
    Cette fonction sert à trouver les coordonnées polaires à partir de coordonnées cartésiennes
    """

    assert (x != 0 or y != 0), "Attention, x et y ne peuvent pas être égaux à 0 en même temps"
    r = np.sqrt(x ** 2 + y ** 2)

    if x == 0 and y > 0:
        delta = 90
    elif x == 0 and y < 0:
        delta = 270
    else:
        delta = np.rad2deg(np.arctan(y / x))

    if x < 0 < y:
        delta += 90
    elif x < 0 and y < 0:
        delta += 180
    elif x > 0 > y:
        delta += 270

    return r, delta

def afficherCourbesRef (nomdefichier : str) :
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

def afficherCourbesMes (nomdefichier : str) :
    ## Cette fonction affiche la courbe mettant en avant l'azimut et la hauteur dans un fichier csv donné

    file = open(nomdefichier,"r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimutList = []
    elevationList = []
    timeList = []

    for m in range (len(data[0])):
        timeList.append(m*5/60)
        x = float(data[0][m])
        y=float(data[1][m])

        r, delta = coordonnes_polaire(x-1024, y-1024)
        
        azimut = delta
        f=2,7
        hauteur = 90 - np.rad2deg(r/f)

        azimutList.append(azimut)
        elevationList.append(hauteur)

        print("x=",x,", y=",y,", r=",r, ", delta=",delta, ", elevation=", hauteur, ", azimut=", azimut)

    plt.plot(timeList, azimutList, label = "Azimut")
    plt.plot(timeList, elevationList, label = "Hauteur")
    
    plt.xlabel('Heure de la journée')
    plt.ylabel('Degré de l\'angle')
    plt.title('Evolution de l\'azimut et la hauteur au cours d\'une journée ')
    plt.legend()
    plt.show()

#afficherCourbesRef(file_ref)
afficherCourbesMes(file_mes)
