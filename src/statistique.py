import numpy as np
from math import *

from afficher_courbes import *
import csv
import copy

##a redéfinir avec les indications du prof
MAPE_max=0.8


def donne_moyenne_decalage_azimut():
    """"donne la moyenne des ecarts entre les valeurs mesurees et celles de reference, pour effectuer la correction """
    Ecarts=donne_decalage_azimut()

    m=0
    for k in range(0,len(Ecarts)):
        m=m+Ecarts[k]
    if len(Ecarts)==0:
        return 0
    else :
        return m/len(Ecarts)



def donne_decalage_azimut():
    """Retourne la liste des decalage pour les differentes valeurs de reference et mesuree, en effectuant un test sur l'erreur quadratique"""
    (x,y)=donne_positions_mesurees()
    (AzimutRef,HauteurRef)=donne_azimut_hauteur_theo()
    (AzimutMes,HauteurMes)=donne_azimut_hauteur_mesurees(x,y)
    Decalage=[]
    ValeursPredites=[]
    ValeursObservees=[]
   

    for k in range(0,len(AzimutRef)):
            
            if valeur_acceptee(AzimutRef[k],AzimutMes[k],ValeursPredites,ValeursObservees):
                Decalage.append(donne_decalage(AzimutRef[k],AzimutMes[k]))
                ValeursPredites.append(AzimutRef[k])
                ValeursObservees.append(AzimutMes[k])
    

    return Decalage



def valeur_acceptee(AzimutRefCourant,AzimutMesCourant,ValeursPredites,ValeursObservees):
    """effectue un test sur les valeurs que l'on va ajouter pour eviter toute valeur aberrante pouvant modifier la callibration"""
    Vp=ValeursPredites.copy()
    Vo=ValeursObservees.copy()

    Vp.append(AzimutRefCourant)
    Vo.append(AzimutMesCourant)
    
    if (AzimutRefCourant == 0) or(AzimutMesCourant== 0):
        return False
    

    ErreurQuadratique=donne_erreur_moyenne_absolue(Vo,Vp)

    if ErreurQuadratique >MAPE_max:
        return False
    
    else:

        return True
    





def donne_erreur_moyenne_absolue(ValeursObservees,ValeursPredites):

    """calcule l'erreur absolue moyenne"""
    erreur=0
    for k in range(0,len(ValeursObservees)):
        erreur=erreur+(abs(ValeursObservees[k]-ValeursPredites[k])/abs(ValeursObservees[k]))

    if len(ValeursObservees)==0:
        return 0
    else:
     

        return erreur/len(ValeursPredites)


def donne_erreur_quadratique(ValeursObservees,ValeursPredites):
    erreur=0
    for k in range(0,len(ValeursObservees)):
        erreur=erreur+((ValeursObservees[k]-ValeursPredites[k])**2)

    if len(ValeursObservees)==0:
        return 0
    else:

        return sqrt(erreur/len(ValeursPredites))





def donne_positions_mesurees():
    """donne la liste des coordonnées x et y a partir du fichier data_mes"""
    f = open("Depot/data_mes.csv","r")
    donnees = list(csv.reader(f, delimiter=","))
   
   
    x=[]
    y=[]

    for k in range(0,len(donnees[0])):
        x.append(float(donnees[0][k]))
        y.append(float(donnees[1][k]))

    f.close()
    return (x,y)


def donne_azimut_hauteur_theo():
    """donne l'azimut et la hauteur de reference du fichier de reference pour chaque point"""
    f= open("Data/data_ref.csv","r")
    donnees = list(csv.reader(f, delimiter=","))
    azimut=[]
    hauteur=[]
    for k in range(0,len(donnees[0])):
        azimut.append(float(donnees[0][k]))
        hauteur.append(float(donnees[1][k]))

    f.close()
    
    return (azimut,hauteur)



def donne_azimut_hauteur_mesurees(x,y):

    """donne l'azimut et la hauteur a partir des listes de points que l'on a obtenu precedemment"""
    Azimut=[]
    Hauteur=[]
    for k in range(0,len(x)):
        x_rot,y_rot=calcul_coordonne_rotation(float(x[k]),float(y[k]),90)
        donnees=calcul_azimut_hauteur(x_rot-1023,y_rot-1023)
        Azimut.append(donnees[0])
        Hauteur.append(donnees[1])
    return (Azimut,Hauteur)




def donne_decalage(a,b):

    """fonction qui sera modifiée en fonction de la façon dont on veut calculer l'erreur dans le jeu de données"""
    return abs(b-a)



def donne_ecartype():
    moyenne=donne_moyenne_decalage_azimut()
    Ecarts=donne_decalage_azimut()
    m=0
    for k in range(0,len(Ecarts)):
        m=m+(Ecarts[k]-moyenne)**2
    return sqrt(m/len(Ecarts))



print(donne_moyenne_decalage_azimut())
