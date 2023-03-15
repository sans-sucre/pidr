import numpy as np
from math import *
#################################Calculs azimut/hauteur



#########################################
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

    if x > 0  > y:
        delta += 180
    elif x > 0 and y > 0:
        delta -= 180

    return r, delta

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

####################Statistiques 


#donne la liste des coordonnées x et y a partir du fichier data_mes
def donnePositionsMesurees():
    file=open("../Depot/data_mes.csv","r")
    donnees_aux=file.readlines()
    donnees=(donnees_aux[0].strip().split(","))
    x=[]
    y=[]


    for k in range(0,int(len(donnees)/2)):
        x.append(int(donnees[k]))
    for l in range(int(len(donnees)/2),len(donnees)):
        y.append(int(donnees[k]))

    return (x,y)

#donne l'azimut et la hauteur de reference du fichier de reference pour chaque point
def donneAzimutHauteurTheo():
    file=open("../Depot/data_ref.csv","r")
    donnees_aux=file.readlines()
    donnees=(donnees_aux[0].strip().split(","))
    azimut=[]
    hauteur=[]
    #print(len(donnees))
    for k in range(0,int(len(donnees)/2)):
        azimut.append(int(donnees[k]))
    for l in range(int(len(donnees)/2),len(donnees)):
        hauteur.append(int(donnees[k]))
    return (azimut,hauteur)


#donne l'azimut et la hauteur a partir des listes de points que l'on a obtenu precedemment
def donneAzimutHauteurMesurees(x,y):
    Azimut=[]
    Hauteur=[]
    for k in range(0,len(x)):
        donnees=calcul_azimut_hauteur(x[k],y[k])
        Azimut.append(donnees[0])
        Hauteur.append(donnees[1])
    return (Azimut,Hauteur)



#Puisque seul l'azimut nous interesse la fonction donne l'ecart entre les azimuts calcules a partir des coordonnees et ceux de reference
def donneEcartsAzimut():
    (x,y)=donnePositionsMesurees()
    (AzimutRef,HauteurRef)=donneAzimutHauteurTheo()
    (AzimutMes,HauteurMes)=donneAzimutHauteurMesurees(x,y)
    Ecarts=[]
    for k in range(0,len(AzimutRef)):
        Ecarts.append(donnEcart(AzimutRef[k],AzimutMes[k]))

    return Ecarts


#fonction qui sera modifiée en fonction de la façon dont on veut calculer l'erreur dans le jeu de données
def donnEcart(a,b):


    return abs(b-a)

#donne la moyenne des ecarts entre les valeurs mesurees et celles de reference, pour effectuer la correction
def donneMoyenneEcartsAzimut():
    Ecarts=donneEcartsAzimut()
    m=0
    for k in range(0,len(Ecarts)):
        m=m+Ecarts[k]
    return m/len(Ecarts)



def donneEcartType():
    moyenne=donneMoyenneEcartsAzimut()
    Ecarts=donneEcartsAzimut()
    m=0
    for k in range(0,len(Ecarts)):
        m=m+(Ecarts[k]-moyenne)**2
    return sqrt(m/len(Ecarts))


print(donneMoyenneEcartsAzimut())
#def donneVariance:
(x,y)=donnePositionsMesurees()
(AzimutMes,HauteurMes)=donneAzimutHauteurMesurees(x,y)
#print(HauteurMes)
#print(512*np.sqrt(2))