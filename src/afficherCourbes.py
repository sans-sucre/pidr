import csv
import numpy as np
import matplotlib.pyplot as plt

file_mes = "data_mes.csv"
file_ref = "data_ref.csv"

import numpy as np

def calcul_coordonne_translation(x: float, y: float, x_translation: float, y_translation: float):
    """Cette fonction sert à calculer les coordonnées après la translation"""

    return x + x_translation, y + y_translation

def calcul_coordonne_rotation(x: float, y: float, angle_rotation: float):
    """Cette fonction sert à calculer les coordonnées après la rotation de certain angle, le paramètre angle_rotation
     est d'unité degré"""

    angle_rotation = np.deg2rad(angle_rotation)
    matrice_rotation = np.array([[np.cos(angle_rotation), (-1) * np.sin(angle_rotation)],
                                 [np.sin(angle_rotation), np.cos(angle_rotation)]])
    x, y = calcul_coordonne_translation(x, y, -1023.5, -1023.5)
    r = np.matmul(matrice_rotation, np.array([x, y]))
    return int(np.rint(r[0] + 1023.5)), int(np.rint(r[1] + 1023.5))

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
        delta += 90
    elif x > 0 > y:
        delta += 270

    return r, delta-90

def calcul_azimut_hauteur(x: float, y: float):
    """
    Cette fonction sert à calculer l'azimute et la hauteur à partir de coordonnées cartésiennes du soleil données.
    L'abscisse doit être le nord magnétique, le point origine doit être le centre d'image. Les paramètres x et y sont
    en mm.
    """

    r, delta = coordonnes_polaire(x, y)
    azimut = delta
    #print("rayon :", r)
    f = 512*np.sqrt(2)
    hauteur = (1-r/f)* 90
    if hauteur < 0 :
        hauteur = 0
    #print("hauteur :", hauteur)
    return azimut, hauteur

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
        x, y = calcul_coordonne_rotation(float(data[0][m]),float(data[1][m]),90)

        azimut, hauteur = calcul_azimut_hauteur(x-1023,y-1023)

        azimutList.append(azimut)
        elevationList.append(hauteur)

        print("x=",x-1023,", y=",y-1023, ", elevation=", hauteur, ", azimut=", azimut)

    plt.plot(timeList, azimutList, label = "Azimut")
    plt.plot(timeList, elevationList, label = "Hauteur")
    
    plt.xlabel('Heure de la journée')
    plt.ylabel('Degré de l\'angle')
    plt.title('Evolution de l\'azimut et la hauteur au cours d\'une journée ')
    plt.legend()
    plt.show()

afficherCourbesRef(file_ref)
afficherCourbesMes(file_mes)