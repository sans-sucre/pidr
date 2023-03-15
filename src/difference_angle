import csv
import numpy as np
import matplotlib.pyplot as plt
from afficherCourbes import calcul_coordonne_rotation, calcul_azimut_hauteur

file_mes = "data_mes.csv"
file_ref = "data_ref.csv"


## Cette fonction renvoie la liste des valeurs d'azimut au cours d'une journée données dans un fichier REFERENCE csv donné
def azimutREF (nomdefichier : str) :

    file = open(nomdefichier,"r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimutList = []

    for m in range (len(data[0])):
        azimutList.append(int(data[0][m]))

    return azimutList

## Cette fonction renvoie la liste des valeurs d'azimut au cours d'une journée données dans un fichier MESURE csv donné
def azimutMES (nomdefichier : str) :

    file = open(nomdefichier,"r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimutList = []

    for m in range (len(data[0])):
        x, y = calcul_coordonne_rotation(float(data[0][m]),float(data[1][m]),90)

        azimut, hauteur = calcul_azimut_hauteur(x-1023,y-1023)

        azimutList.append(azimut)

    return azimutList

## Cette fonction renvoie la différence d'angle entre l'azimut du fichier de REFERENCE et celui MESURE
def donneEcartsAzimut(nomdefichierREF : str, nomdefichierMES : str):
    Ecarts=[]

    a_ref = azimutREF(nomdefichierREF)
    a_mes = azimutMES(nomdefichierMES)

    for m in range(len(a_ref)):
        if (a_ref[m] != 0) and (a_mes[m] != 0):
            Ecarts.append(abs(a_ref[m]-a_mes[m]))

    moyenne = 0

    for k in range(len(Ecarts)):
        moyenne=moyenne+Ecarts[k]

    return moyenne/len(Ecarts)

print(donneEcartsAzimut(file_ref, file_mes))

