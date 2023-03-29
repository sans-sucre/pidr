import numpy as np
from math import *
import csv
import copy

##a redéfinir avec les indications du prof
MAPE_max=0.3



################fonction principale


#donne la moyenne des ecarts entre les valeurs mesurees et celles de reference, pour effectuer la correction
def donneMoyenneDecalageAzimut():
    Ecarts=donneDecalageAzimut()
    m=0
    for k in range(0,len(Ecarts)):
        m=m+Ecarts[k]
    if len(Ecarts)==0:
        return 0
    else :
        return m/len(Ecarts)

####################Annexes

#Retourne la liste des decalage pour les differentes valeurs de reference et mesuree, en effectuant un test sur l'erreur quadratique
def donneDecalageAzimut():
    (x,y)=donnePositionsMesurees()
    (AzimutRef,HauteurRef)=donneAzimutHauteurTheo()
    (AzimutMes,HauteurMes)=donneAzimutHauteurMesurees(x,y)
    Decalage=[]
    ValeursPredites=[]
    ValeursObservees=[]
    print(len(AzimutRef))

    for k in range(0,len(AzimutRef)):
            
            if valeurAcceptee(AzimutRef[k],AzimutMes[k],ValeursPredites,ValeursObservees):
                Decalage.append(donneDecalage(AzimutRef[k],AzimutMes[k]))
                ValeursPredites.append(AzimutRef[k])
                ValeursObservees.append(AzimutMes[k])
    

    print(len(ValeursObservees))
    return Decalage


#effectue un test sur les valeurs que l'on va ajouter pour eviter toute valeur aberrante pouvant modifier la callibration

def valeurAcceptee(AzimutRefCourant,AzimutMesCourant,ValeursPredites,ValeursObservees):
    Vp=ValeursPredites.copy()
    Vo=ValeursObservees.copy()

    Vp.append(AzimutRefCourant)
    Vo.append(AzimutMesCourant)
    
    if (AzimutRefCourant == 0) or(AzimutMesCourant== 0):
        return False
    

    ErreurQuadratique=donneErreurMoyenneAbsolue(Vo,Vp)

    if ErreurQuadratique >MAPE_max:
        return False
    
    else:

        return True
    



#calcule l'erreur absolue moyenne

def donneErreurMoyenneAbsolue(ValeursObservees,ValeursPredites):
    erreur=0
    for k in range(0,len(ValeursObservees)):
        erreur=erreur+(abs(ValeursObservees[k]-ValeursPredites[k])/abs(ValeursObservees[k]))

    if len(ValeursObservees)==0:
        return 0
    else:
        print(erreur/len(ValeursPredites))

        return erreur/len(ValeursPredites)


def donneErreurQuadratique(ValeursObservees,ValeursPredites):
    erreur=0
    for k in range(0,len(ValeursObservees)):
        erreur=erreur+((ValeursObservees[k]-ValeursPredites[k])**2)

    if len(ValeursObservees)==0:
        return 0
    else:

        return sqrt(erreur/len(ValeursPredites))




#donne la liste des coordonnées x et y a partir du fichier data_mes
def donnePositionsMesurees():

    f = open("../Depot/data_mes.csv","r")
    donnees = list(csv.reader(f, delimiter=","))
   
   
    x=[]
    y=[]

    for k in range(0,len(donnees[0])):
        x.append(int(donnees[0][k]))
        y.append(int(donnees[1][k]))

    f.close()
    return (x,y)

#donne l'azimut et la hauteur de reference du fichier de reference pour chaque point
def donneAzimutHauteurTheo():
    f= open("../Depot/data_ref.csv","r")
    donnees = list(csv.reader(f, delimiter=","))
    azimut=[]
    hauteur=[]
    for k in range(0,len(donnees[0])):
        azimut.append(int(donnees[0][k]))
        hauteur.append(int(donnees[1][k]))

    f.close()
    
    return (azimut,hauteur)


#donne l'azimut et la hauteur a partir des listes de points que l'on a obtenu precedemment
def donneAzimutHauteurMesurees(x,y):
    Azimut=[]
    Hauteur=[]
    for k in range(0,len(x)):
        x_rot,y_rot=calcul_coordonne_rotation(float(x[k]),float(y[k]),90)
        donnees=calcul_azimut_hauteur(x_rot-1023,y_rot-1023)
        Azimut.append(donnees[0])
        Hauteur.append(donnees[1])
    return (Azimut,Hauteur)



#fonction qui sera modifiée en fonction de la façon dont on veut calculer l'erreur dans le jeu de données
def donneDecalage(a,b):
    return abs(b-a)



def donneEcartType():
    moyenne=donneMoyenneDecalageAzimut()
    Ecarts=donneDecalageAzimut()
    m=0
    for k in range(0,len(Ecarts)):
        m=m+(Ecarts[k]-moyenne)**2
    return sqrt(m/len(Ecarts))



#################################Calculs azimut/hauteur

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





########################################################################Test

print(donneMoyenneDecalageAzimut())
#def donneVariance:
#(x,y)=donnePositionsMesurees()
#(AzimutMes,HauteurMes)=donneAzimutHauteurMesurees(x,y)
#print(HauteurMes)
#print(512*np.sqrt(2))

#liste=[9,15,20,24,29,36,42,43,52,54]

#liste2=[10,15,20,25,30,35,40,45,50,55]

#print(donneErreurQuadratique(liste,liste2))