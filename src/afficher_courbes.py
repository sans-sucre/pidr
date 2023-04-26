import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from calcul_azimute_hauteur import calcul_azimut_hauteur

#file_mes = "Data/data_mes.csv"
#file_ref = "Data/data_web.csv"

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

        azimut, hauteur = calcul_azimut_hauteur(float(data[0][m])-1023,float(data[1][m])-1023,90)

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

#afficherCourbesMes(file_mes)

##afficherParcours(file_ref,file_mes)

if __name__ == '__main__':
    file_ref = sys.argv[1]
    file_mes = sys.argv[2]
    afficherCourbesRef(file_ref)
    afficherCourbesMes(file_mes)
    afficherParcours(file_ref, file_mes)