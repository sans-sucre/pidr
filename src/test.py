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
