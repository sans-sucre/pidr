import math

#Donne les coordonnées du point après une rotation, peut être utilisé comme une fonction annexe
#Dans le cas pratique on devra donner l'axe par lequel on tourne 

def rotation(x_ini,y_ini,angle,x_rotation,y_rotation):

    x_ur=x_ini-x_rotation #vecteur translation base polaire
    y_ur=y_ini -y_rotation #vecteur translation base polaire

    x_teta=math.cos(angle)*x_ur -math.sin(angle)*y_ur #vecteur rotation base polaire
    y_teta=math.sin(angle)*x_ur +math.cos(angle)*y_ur #vecteur rotation base polaire


    x_rotation= x_ini+x_teta #calcul du point après modification 
    y_rotation=y_ini+y_teta

    return (x_rotation,y_rotation)