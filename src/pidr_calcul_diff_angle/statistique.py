import numpy as np
from math import *

from afficher_courbes import *
import csv
from math import *

from src.pidr_calcul_diff_angle.afficher_courbes import *

# à redéfinir avec les indications du prof
mape_max = 0.9
seuil_modelisation = 0.1
file_mes = "Data/data_mes.csv"
file_ref = "Data/data_ref.csv"


def donne_moyenne_decalage_azimut(fichier1, fichier2):
    """"Donner la moyenne des écarts entre les valeurs mesurées
     et celles de reference, pour effectuer la correction """

    ecarts = donne_decalage_azimut(fichier1, fichier2)

    m = 0
    for k in range(0, len(ecarts)):
        m = m + ecarts[k]
    if len(ecarts) == 0:
        return 0
    else:
        return m / len(ecarts)


def donne_moyenne_decalage_azimut_corrige(fichier1, fichier2, MAPE_max):
    """"Donner la moyenne des écarts entre les valeurs mesurées et celles de
    reference, pour effectuer la correction après
    suppression des valeurs aberrantes (utilisation de l'erreur absolue moyenne) """

    ecarts = donne_decalage_azimut_corrige(fichier1, fichier2, MAPE_max)

    m = 0
    for k in range(0, len(ecarts)):
        m = m + ecarts[k]
    if len(ecarts) == 0:
        return 0
    else:
        return m / len(ecarts)


def donne_decalage_azimut(fichier1, fichier2):
    """Retourne la liste des decalage pour les differentes
    valeurs de reference et mesuree, en enlevant les valeurs de nuit"""

    (x, y) = donne_positions_mesurees(fichier2)
    (AzimutRef, HauteurRef) = donne_azimut_hauteur_theo(fichier1)
    (AzimutMes, HauteurMes) = donne_azimut_hauteur_mesurees(x, y)
    decalage = []
    valeurs_predites = []
    valeurs_observees = []

    for k in range(0, len(AzimutRef)):

        if valeur_acceptee(AzimutRef[k], AzimutMes[k], valeurs_predites, valeurs_observees):
            decalage.append(donne_decalage(AzimutRef[k], AzimutMes[k]))
            valeurs_predites.append(AzimutRef[k])
            valeurs_observees.append(AzimutMes[k])

    return decalage


def donne_decalage_azimut_corrige(fichier1, fichier2, mape_max):
    """Retourne la liste des decalage pour les differentes valeurs
    de reference et mesuree, en effectuant un test sur l'erreur absolue moyenne"""

    (x, y) = donne_positions_mesurees(fichier2)
    (AzimutRef, HauteurRef) = donne_azimut_hauteur_theo(fichier1)
    (AzimutMes, HauteurMes) = donne_azimut_hauteur_mesurees(x, y)
    decalage = []
    valeurs_predites = []
    valeurs_observees = []

    for k in range(0, len(AzimutRef)):

        if valeur_acceptee_MAPE(AzimutRef[k], AzimutMes[k], valeurs_predites, valeurs_observees, mape_max):
            decalage.append(donne_decalage(AzimutRef[k], AzimutMes[k]))
            valeurs_predites.append(AzimutRef[k])
            valeurs_observees.append(AzimutMes[k])

    return decalage

    return Decalage

def valeur_acceptee(azimut_ref_courant, azimut_mes_courant, valeurs_predites, valeurs_observees):
    """Effectuer un test sur les valeurs que l'on
    va ajouter pour eviter toute valeur aberrante pouvant modifier la callibration"""

    vp = valeurs_predites.copy()
    vo = valeurs_observees.copy()

    vp.append(azimut_ref_courant)
    vo.append(azimut_mes_courant)

    if (azimut_ref_courant == 0) or (azimut_mes_courant == 0):
        return False
    else:
        return True


def valeur_acceptee_MAPE(azimut_ref_courant, azimut_mes_courant, valeurs_predites, valeurs_observees, mape_max):
    """effectue un test sur les valeurs que l'on va ajouter pour eviter toute
    valeur aberrante pouvant modifier la callibration en utilisant l'erreur moyenne absolue  """

    vp = valeurs_predites.copy()
    vo = valeurs_observees.copy()

    vp.append(azimut_ref_courant)
    vo.append(azimut_mes_courant)

    if (azimut_ref_courant == 0) or (azimut_mes_courant == 0):
        return False

    else:
        erreur_quadratique = donne_erreur_moyenne_absolue(vo, vp)

        if erreur_quadratique >= mape_max:
            return False

        else:

            return True
    


def donne_erreur_moyenne_absolue(valeurs_observees, valeurs_predites):
    """calcule l'erreur absolue moyenne"""
    erreur = 0
    for k in range(0, len(valeurs_observees)):
        if valeurs_observees[k] != 0:
            erreur = erreur + (abs(valeurs_observees[k] - valeurs_predites[k]) / abs(valeurs_observees[k]))

    if len(valeurs_observees) == 0:
        return 0
    else:

        return erreur / len(valeurs_predites)


def donne_positions_mesurees(fichier2):
    """Donner la liste des coordonnées x et y à
     partir du fichier data_mes"""

    f = open(fichier2, "r")
    donnees = list(csv.reader(f, delimiter=","))

    x = []
    y = []

    for k in range(0, len(donnees[0])):
        x.append(float(donnees[0][k]))
        y.append(float(donnees[1][k]))

    f.close()
    return (x, y)


def donne_azimut_hauteur_theo(file):
    """Donner l'azimut et la hauteur de reference
    du fichier de reference tiré de la modélisation pour chaque point"""
    f = open(file, "r")
    donnees = list(csv.reader(f, delimiter=","))
    azimut = []
    hauteur = []
    for k in range(0, len(donnees[0])):
        azimut.append(float(donnees[0][k]))
        hauteur.append(float(donnees[1][k]))

    f.close()

    return azimut, hauteur


def donne_azimut_hauteur_mesurees(x, y):
    """Donner l'azimut et la hauteur a partir des listes de points que l'on a obtenu précédemment"""
    azimut = []
    hauteur = []
    for k in range(0, len(x)):
        donnees = calcul_azimut_hauteur(x[k] - 1023, y[k] - 1023, 0)
        azimut.append(donnees[0])
        hauteur.append(donnees[1])
    return azimut, hauteur


def donne_decalage(a, b):
    """Fonction qui sera modifiée en fonction de la façon dont on veut calculer l'erreur dans le jeu de données"""
    return abs(b - a)


def donne_ecartype():
    """Donner l'ecartype pour faire une interprétation des résultats, mais ce n'est pas utilisé pour l'instant"""
    moyenne = donne_moyenne_decalage_azimut()
    ecarts = donne_decalage_azimut()
    m = 0
    for k in range(0, len(ecarts)):
        m = m + (ecarts[k] - moyenne) ** 2
    return sqrt(m / len(ecarts))


def modelisation_correcte(fichier1, fichier2, seuil_modelisation):
    """Permettre de tester si la modélisation et correcte en calculant l'erreur moyenne
     et vérifiant si elle est inférieur à 0 pourcent. En entree, il y a le fichier de donnees
    du web et le fichier de données de la modélisation que l'on veut comparer
    """

    azimut_web, hauteur_web = donne_azimut_hauteur_theo(fichier1)
    azimut_mod, hauteur_mod = donne_azimut_hauteur_theo(fichier2)

    erreur_azimut = 0
    erreur_hauteur = 0
    for k in range(0, len(azimut_mod)):
        erreur_azimut += abs(azimut_web[k] - azimut_mod[k])
        erreur_hauteur += abs(hauteur_web[k] - hauteur_mod[k])

    if len(azimut_mod) > 0:
        erreur_azimut = erreur_azimut / len(azimut_mod)
        erreur_hauteur = erreur_hauteur / len(azimut_mod)

    print(f"erreur sur l'azimut :{erreur_azimut}")
    print(f"erreur sur la hauteur :{erreur_hauteur}")

    if erreur_azimut > seuil_modelisation or erreur_hauteur > seuil_modelisation:
        s = "La modélisation n'est pas correcte"
    else:
        s = "La modélisation est correcte"

    return s


if __name__ == '__main__':
    if len(sys.argv) >= 4:

        print(sys.argv[1])
        if sys.argv[1] == "-modelisation":
            file_ref = sys.argv[2]
            file_mes = sys.argv[3]
            if len(sys.argv) >= 6 and sys.argv[4] == "-niveau":
                seuil_modelisation = float(sys.argv[5])
                print(modelisation_correcte(file_ref, file_mes, seuil_modelisation))
            else:
                print(modelisation_correcte(file_ref, file_mes, 0.5))

        if sys.argv[1] == "-decalage":

            file_ref = sys.argv[2]
            file_mes = sys.argv[3]
            if len(sys.argv) >= 6 and sys.argv[4] == "-correction":
                mape_max = float(sys.argv[5])

                print(donne_moyenne_decalage_azimut_corrige(file_ref, file_mes, mape_max))

            else:

                print(donne_moyenne_decalage_azimut(file_ref, file_mes))

    else:
        print("Veuillez renseigner tous les paramètres. Tapez '-info' pour plus d'aide")
