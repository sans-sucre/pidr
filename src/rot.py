import math
import numpy as np


#Pour un point de l'image (2 dimensions) donne la matrice de rotation correspondant à l'angle
#en degré
def giveRotationMatrix(angle):
    teta=math.radians(angle)

    Rotation_matrix=[[math.cos(teta) -math.sin(teta)],[math.sin(teta) math.cos(teta)]]
    return Rotation_matrix



print(giveRotationMatrix(90))