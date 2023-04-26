import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

#file_mes = "Data/data_mes.csv"
#file_ref = "Data/data_web.csv"


# Calculs sur les coordonées

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

    if x > 0 > y:
        delta += 180
    elif x > 0 and y > 0:
        delta -= 180

    return r, delta

def coordonnees_cartesiennes(r: float, theta: float) :
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return x,y


# Calcul de l'azimut et de la hauteur

def calcul_azimut_hauteur(x: float, y: float):
    """
    Cette fonction sert à calculer l'azimute et la hauteur à partir de coordonnées cartésiennes du soleil données.
    L'abscisse doit être le nord magnétique, le point origine doit être le centre d'image. Les paramètres x et y sont
    en mm.
    """

    r, delta = coordonnes_polaire(x, y)
    azimut = delta
    f = 512*np.sqrt(2)
    hauteur = (1-r/f)* 90
    if hauteur < 0 :
        hauteur = 0
    return azimut, hauteur

def calcul_aziHaut_to_cart(a: float, h: float):
    """
    Cette fonction sert à calculer les coordonées x et y du soleil à partir de l'azimut et la hauteur.
    """
    f = 512*np.sqrt(2)

    r = f*(1-h/90)
    theta = a

    x,y= coordonnees_cartesiennes(r,np.deg2rad(theta-90))
    return x, y


# Affichage des courbes

def afficherCourbesRef (nomdefichier : str) :
    """ Cette fonction affiche la courbe mettant en avant l'azimut et la hauteur dans un fichier csv donné"""

    file = open(nomdefichier,"r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    azimutList = []
    elevationList = []
    timeList = []
    
    for m in range (len(data[0])):
        timeList.append(m*5/60)
        if (float(data[0][m])>0) :
            azimutList.append(float(data[0][m])-180)
        elif (float(data[0][m])<0) :
            azimutList.append(float(data[0][m])+180)
        else :
            azimutList.append(float(data[0][m]))
        elevationList.append(float(data[1][m]))

    plt.plot(timeList, azimutList, label = "Azimut")
    plt.plot(timeList, elevationList, label = "Hauteur")
    
    plt.xlabel('Heure de la journée')
    plt.ylabel('Degré de l\'angle')
    plt.title('Evolution de l\'azimut et la hauteur au cours d\'une journée ')
    plt.legend()
    plt.savefig("Data/courbeAzElREF.png")
    plt.show()
    
def afficherCourbesMes (nomdefichier : str) :
    """ Cette fonction affiche la courbe mettant en avant l'azimut et la hauteur dans un fichier csv donné"""

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

    plt.plot(timeList, azimutList, label = "Azimut")
    plt.plot(timeList, elevationList, label = "Hauteur")
    
    plt.xlabel('Heure de la journée')
    plt.ylabel('Degré de l\'angle')
    plt.title('Evolution de l\'azimut et la hauteur au cours d\'une journée ')
    plt.legend()
    plt.savefig("Data/courbeAzElMES.png")
    plt.show()

def afficherParcours (nomdefichierREF : str, nomdefichierMES : str) :
    """ Cette fonction affiche le parcours du soleil à l'aide de fichiers de REF (contenant des azimuts et hauteurs) et un fichier MES (contenant des coordonnées x et y). """

    fileMES = open(nomdefichierMES,"r")
    dataMES = list(csv.reader(fileMES, delimiter=","))
    fileMES.close()

    fileREF = open(nomdefichierREF,"r")
    dataREF = list(csv.reader(fileREF, delimiter=","))
    fileREF.close()

    xListMES = []
    yListMES = []

    xListREF = []
    yListREF = []

    for m in range (len(dataMES[0])):
        #Partie des données mesurées
        x, y = calcul_coordonne_rotation(float(dataMES[0][m]),float(dataMES[1][m]),180)
        x=x-1023
        y=y-1023

        if (x*x + y*y <= 700*700) :
            xListMES.append(x)
            yListMES.append(y)

    for m in range (len(dataREF[0])):
        #Partie des données de référence :
        a, h = float(dataREF[0][m]),float(dataREF[1][m])
        x_ref, y_ref = calcul_aziHaut_to_cart(a,h)

        if (x_ref*x_ref + y_ref*y_ref <= 700*700) :
            xListREF.append(x_ref)
            yListREF.append(y_ref)

    plt.figure(figsize=(7,7))
    plt.plot(xListMES, yListMES, label = "Valeurs Mesurées")
    plt.plot(xListREF, yListREF, label = "Valeurs Théoriques")
    plt.plot(700*np.cos(np.linspace(0,2*np.pi,150)), 700*np.sin(np.linspace(0,2*np.pi,150)))

    plt.xlim(-800,800)
    plt.ylim(-800,800)

    plt.title('Parcours du soleil au cours d\'une journée ')
    plt.legend()
    plt.savefig("Data/parcoursSoleil.png")
    plt.show()

##afficherCourbesRef(file_ref)

##afficherCourbesMes(file_mes)

##afficherParcours(file_ref,file_mes)

if __name__ == '__main__':
    file_ref = sys.argv[1]
    file_mes = sys.argv[2]
    afficherCourbesRef(file_ref)
    afficherCourbesMes(file_mes)
    afficherParcours(file_ref, file_mes)