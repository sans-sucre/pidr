import numpy as np
from math import *

from afficher_courbes import *
import csv
import copy

##a redéfinir avec les indications du prof
MAPE_max=0.9
seuil_modelisation=0.1
file_mes = "Data/data_mes.csv"
file_ref = "Data/data_ref.csv"



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
    (AzimutRef,HauteurRef)=donne_azimut_hauteur_theo(file_ref)
    (AzimutMes,HauteurMes)=donne_azimut_hauteur_mesurees(x,y)
    Decalage=[]
    ValeursPredites=[]
    ValeursObservees=[]
   

    for k in range(0,len(AzimutRef)):
            
            if valeur_acceptee_MAPE(AzimutRef[k],AzimutMes[k],ValeursPredites,ValeursObservees):
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
    
    
    else:

        return True
    
def valeur_acceptee_MAPE(AzimutRefCourant,AzimutMesCourant,ValeursPredites,ValeursObservees):

    """effectue un test sur les valeurs que l'on va ajouter pour eviter toute valeur aberrante pouvant modifier la callibration"""

    Vp=ValeursPredites.copy()
    Vo=ValeursObservees.copy()

    Vp.append(AzimutRefCourant)
    Vo.append(AzimutMesCourant)
    
    if (AzimutRefCourant == 0) or(AzimutMesCourant== 0):
        return False
    

    ErreurQuadratique=donne_erreur_moyenne_absolue(Vo,Vp)

    if ErreurQuadratique >=MAPE_max :
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

    f = open(file_mes,"r")
    donnees = list(csv.reader(f, delimiter=","))
   
   
    x=[]
    y=[]

    for k in range(0,len(donnees[0])):
        x.append(float(donnees[0][k]))
        y.append(float(donnees[1][k]))

    f.close()
    return (x,y)


def donne_azimut_hauteur_theo(file):
    """donne l'azimut et la hauteur de reference du fichier de reference tiré de la modélistion pour chaque point"""
    f= open(file,"r")
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
        donnees=calcul_azimut_hauteur(x[k]-1023,y[k]-1023,0)
        Azimut.append(donnees[0])
        Hauteur.append(donnees[1])
    return (Azimut,Hauteur)




def donne_decalage(a,b):

    """fonction qui sera modifiée en fonction de la façon dont on veut calculer l'erreur dans le jeu de données"""
    return abs(b-a)



def donne_ecartype():

    """donne l'ecartype pour faire une interprétation des résultats mais ce n'est pas utilisé pour l'instant"""
    moyenne=donne_moyenne_decalage_azimut()
    Ecarts=donne_decalage_azimut()
    m=0
    for k in range(0,len(Ecarts)):
        m=m+(Ecarts[k]-moyenne)**2
    return sqrt(m/len(Ecarts))





def modelisation_correcte():
 
    """permet de tester si la modélisation et correcte en calculant l'erreur moyenne et verifiant si elle est inferieur à 0 pourcent .
    En entree il y a le fichier de donnees du web et le fichier de donnees de la modelisation que l'on veut comparer 
    """

    azimut_web,hauteur_web=donne_azimut_hauteur_theo(file_ref)
    azimut_mod,hauteur_mod=donne_azimut_hauteur_theo(file_mes)

    erreur_azimut=0
    erreur_hauteur=0
    for k in range(0,len(azimut_mod)):
        erreur_azimut+=azimut_web[k]-azimut_mod[k]
        erreur_hauteur+=hauteur_web[k]- hauteur_mod[k]

    if len(azimut_mod)>0:
        erreur_azimut=erreur_azimut/len(azimut_mod)
        erreur_hauteur=erreur_hauteur/len(azimut_mod)

    print(f"erreur sur l'azimut :{erreur_azimut}")
    print(f"erreur sur la hauteur :{erreur_hauteur}")

    if (erreur_azimut>seuil_modelisation or erreur_hauteur>seuil_modelisation):
        print("La modélisation n'est pas correcte")
    else :
        print("La modélisation est correcte")

    return





print(donne_moyenne_decalage_azimut())




if __name__ == '__main__':
    if len(sys.argv)>=2:
       file_ref = sys.argv[1]
       file_mes = sys.argv[2]





