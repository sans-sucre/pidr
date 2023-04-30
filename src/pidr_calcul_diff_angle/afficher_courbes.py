import csv

import matplotlib.pyplot as plt
import numpy as np

from src.pidr_calcul_diff_angle.calcul_azimute_hauteur import calcul_azimut_hauteur


# file_mes = "Data/data_mes.csv"
# file_ref = "Data/data_web.csv"

# Calculs sur les coordonnées

def calcul_coordonne_translation(x: float, y: float, x_translation: float, y_translation: float):
    """Cette fonction sert à calculer les coordonnées après la translation"""

    return x + x_translation, y + y_translation


def calcul_coordonne_rotation(x: float, y: float, angle_rotation: float):
    """Cette fonction sert à calculer les coordonnées
     après la rotation de certain angle, le paramètre angle_rotation
     est d'unité degré"""

    angle_rotation = np.deg2rad(angle_rotation)
    matrice_rotation = np.array([[np.cos(angle_rotation), (-1) * np.sin(angle_rotation)],
                                 [np.sin(angle_rotation), np.cos(angle_rotation)]])
    x, y = calcul_coordonne_translation(x, y, -1023.5, -1023.5)
    r = np.matmul(matrice_rotation, np.array([x, y]))
    return int(np.rint(r[0] + 1023.5)), int(np.rint(r[1] + 1023.5))


def coordonnes_polaire(x: float, y: float):
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

    if x > 0 > y:
        delta += 180
    elif x > 0 and y > 0:
        delta -= 180

    return r, delta


def coordonnees_cartesiennes(r: float, theta: float):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


# Calcul de l'azimut et de la hauteur

def calcul_azi_haut_to_cart(a: float, h: float):
    """
    Cette fonction sert à calculer les coordonnées x et y du soleil à partir de l'azimut et la hauteur.
    """
    f = 512 * np.sqrt(2)

    r = f * (1 - h / 90)
    theta = a

    x, y = coordonnees_cartesiennes(r, np.deg2rad(theta - 90))
    return x, y


# Affichage des courbes

def afficher_courbes_ref(nom_fichier: str):
    """ Cette fonction affiche la courbe mettant en avant l'azimut et la hauteur dans
    un fichier csv donné, contenant en première ligne les azimuts et en deuxième les hauteurs."""

    file = open(nom_fichier, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimut_list = []
    elevation_list = []
    time_list = []

    for m in range(len(data[0])):
        time_list.append(m * 5 / 60)
        if float(data[0][m]) > 0:
            azimut_list.append(float(data[0][m]) - 180)
        elif float(data[0][m]) < 0:
            azimut_list.append(float(data[0][m]) + 180)
        else:
            azimut_list.append(float(data[0][m]))
        elevation_list.append(float(data[1][m]))

    plt.plot(time_list, azimut_list, label="Azimut")
    plt.plot(time_list, elevation_list, label="Hauteur")

    plt.xlabel('Heure de la journée')
    plt.ylabel('Degré de l\'angle')
    plt.title('Evolution de l\'azimut et la hauteur')
    plt.legend()
    plt.savefig("Images/azimutHauteurFichierRef.png")
    # plt.show()


def afficher_courbes_mes(nom_fichier: str):
    """ Cette fonction affiche la courbe mettant en avant l'azimut et
    la hauteur dans un fichier csv donné, contenant en première ligne les x et en deuxième les y."""

    file = open(nom_fichier, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimut_list = []
    elevation_list = []
    time_list = []

    for m in range(len(data[0])):
        time_list.append(m * 5 / 60)

        azimut, hauteur = calcul_azimut_hauteur(float(data[0][m]) - 1023, float(data[1][m]) - 1023, 90)

        azimut_list.append(azimut)
        if hauteur < 0:
            hauteur = 0
        elevation_list.append(hauteur)

    plt.plot(time_list, azimut_list, label="Azimut")
    plt.plot(time_list, elevation_list, label="Hauteur")

    plt.xlabel('Heure de la journée')
    plt.ylabel('Degré de l\'angle')
    plt.title('Evolution de l\'azimut et la hauteur')
    plt.legend()
    plt.savefig("Images/azimutHauteurFichierMesures.png")
    # plt.show()


def afficher_parcours(fichier_ref: str, fichier_mes: str) -> None:
    """ Cette fonction affiche le parcours du soleil à l'aide de fichiers
     de REF (contenant des azimuts et hauteurs) et un fichier MES (contenant des coordonnées x et y). """

    file_mes = open(fichier_mes, "r")
    data_mes = list(csv.reader(file_mes, delimiter=","))
    file_mes.close()

    file_ref = open(fichier_ref, "r")
    data_ref = list(csv.reader(file_ref, delimiter=","))
    file_ref.close()

    x_list_mes = []
    y_list_mes = []

    x_list_ref = []
    y_list_ref = []

    for m in range(len(data_mes[0])):
        # Partie des données mesurées
        x, y = calcul_coordonne_rotation(float(data_mes[0][m]), float(data_mes[1][m]), 180)
        x = x - 1023
        y = y - 1023

        if x * x + y * y <= 700 * 700:
            x_list_mes.append(x)
            y_list_mes.append(y)

    for m in range(len(data_ref[0])):
        # Partie des données de référence :
        a, h = float(data_ref[0][m]), float(data_ref[1][m])
        if a > 0:
            a = (a - 180)
        elif a < 0:
            a = a + 180
        x_ref, y_ref = calcul_azi_haut_to_cart(a, h)

        if x_ref * x_ref + y_ref * y_ref <= 700 * 700:
            x_list_ref.append(x_ref)
            y_list_ref.append(y_ref)

    plt.figure(figsize=(7, 7))
    plt.plot(x_list_mes, y_list_mes, label="Valeurs Mesurées")
    plt.plot(x_list_ref, y_list_ref, label="Valeurs Théoriques")
    plt.plot(700 * np.cos(np.linspace(0, 2 * np.pi, 150)), 700 * np.sin(np.linspace(0, 2 * np.pi, 150)))

    plt.xlim(-800, 800)
    plt.ylim(-800, 800)

    plt.title('Parcours du soleil')
    plt.legend()
    plt.savefig("Images/parcoursSoleil.png")
    # plt.show()

##afficherCourbesRef(file_ref)

##afficherCourbesMes(file_mes)

# afficherParcours(file_ref,file_mes)

# if __name__ == '__main__':
#    file_ref = sys.argv[1]
#    file_mes = sys.argv[2]
#    afficherCourbesRef(file_ref)
#    afficherCourbesMes(file_mes)
#    afficherParcours(file_ref, file_mes)
