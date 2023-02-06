import numpy
import math
#phi la latitude, je sais pas encore ce qui correspond au declinaison et a h
def giveAzimutAndElevation(phi,H,D):
    hauteur=math.degrees(math.asin(math.sin(math.radians(D))*math.sin(phi)+math.cos(math.radians(D))*math.cos(phi)*math.cos(math.radians(H))))
    if hauteur>=0:# élimine les hauteurs négatives (soleil couché)
                hauteur=-1
    azimut=math.degrees(math.atan(math.sin(math.radians(H))/(math.sin(phi)*math.cos(math.radians(hauteur))-math.cos(phi)*math.tan(math.radians(D)))))
    if azimut<0 and hauteur>0:#tests de valeurs d'azimut
        azimut=azimut+180
    else:
        if azimut>0 and azimut<0:
            azimut=azimut-180
    return (azimut,hauteur)
import math

#Donne les coordonnées du point après une rotation, peut être utilisé comme une fonction annexe
#Dans le cas pratique on devra donner l'axe par lequel on tourne ici ce sera sur l'axe des x et le nord sera sur l'axe des y

def rotation(x_ini,y_ini,angle,x_rotation,y_rotation):
    angle=(angle*math.pi)/180

    x_ur=x_ini-x_rotation #vecteur translation base polaire
    y_ur=y_ini -y_rotation #vecteur translation base polaire

    x_teta=math.cos(angle)*x_ur -math.sin(angle)*y_ur #vecteur rotation base polaire
    y_teta=math.sin(angle)*x_ur +math.cos(angle)*y_ur #vecteur rotation base polaire


    x_rotation= x_ini+x_teta #calcul du point après modification 
    y_rotation=y_ini+y_teta

    print(angle,2*math.pi)


    return (math.round(x_rotation),math.round(y_rotation))


#Donne les coordonnées du point translaté, peut être utilisé comme une fonction annexe
#Dans le cas pratique on aura juste le vecteur de translation et on adaptera
def translation (x_ini,y_ini,x_translation,y_translation):

    x_translation= x_ini+x_translation
    y_translation=y_ini+y_translation

    return (x_translation,y_translation)



print(translation(1,-1,0,1))


rotation(0,0,360,0,1)
