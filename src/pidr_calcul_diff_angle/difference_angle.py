import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from src.pidr_calcul_diff_angle.afficher_courbes import calcul_coordonne_rotation
from src.pidr_calcul_diff_angle.calcul_azimute_hauteur import calcul_azimut_hauteur

file_mes = "Data/data_mes.csv"
file_ref = "Data/data_web.csv"


def azimut_ref(nom_fichier: str):
    """Cette fonction renvoie la liste des valeurs d'azimut
    au cours d'une journée données dans un fichier REFERENCE csv donné"""

    file = open(nom_fichier, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimut_list = []

    for m in range(len(data[0])):
        if float(data[0][m]) > 0:
            azimut_list.append(float(data[0][m])-180)
        elif float(data[0][m]) < 0:
            azimut_list.append(float(data[0][m])+180)
        else:
            azimut_list.append(float(data[0][m]))

    return azimut_list


def azimut_mes(nom_fichier: str):
    """Cette fonction renvoie la liste des valeurs d'azimut
     au cours d'une journée données dans un fichier MESURE csv donné"""

    file = open(nom_fichier, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimut_list = []

    for m in range (len(data[0])):
        x, y = calcul_coordonne_rotation(float(data[0][m]), float(data[1][m]), 90)

        azimut, hauteur = calcul_azimut_hauteur(x-1023, y-1023, 90)

        azimut_list.append(azimut)

    return azimut_list


def donne_ecarts_azimut(fichier_ref: str, fichier_mes: str):
    """Cette fonction renvoie la différence d'angle entre l'azimut du fichier de REFERENCE et celui MESURE"""

    ecarts = []

    a_ref = azimut_ref(fichier_ref)
    a_mes = azimut_mes(fichier_mes)

    for m in range(len(a_ref)):
        if (a_ref[m] != 0) and (a_mes[m] != 0):
            ecarts.append(abs(a_ref[m]-a_mes[m]))

    moyenne = 0

    for k in range(len(ecarts)):
        moyenne = moyenne+ecarts[k]

    return moyenne/len(ecarts)

# print(donneEcartsAzimut(file_ref, file_mes))


# if __name__ == '__main__':
#    file_ref = sys.argv[1]
#    file_mes = sys.argv[2]
#    result = donne_ecarts_azimut(file_ref, file_mes)
#    print(result)
