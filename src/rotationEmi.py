import math
import random
import numpy as np
from matplotlib import pyplot as plt

#Pour un point de l'image (2 dimensions) donne la matrice de rotation correspondant à l'angle
#en degré
def giveRotationMatrix(angle):
    teta=math.radians(angle)

    Rotation_matrix=[[round(math.cos(teta) ),-round(math.sin(teta))],[round(math.sin(teta)) ,round(math.cos(teta))]]
    return Rotation_matrix

#donne les coordonnées du pixel après rotation
def rotatePixelCoordonate(angle,x,y):
    Point=[x,y]
    rotationMatrix=giveRotationMatrix(angle)
    return rotationMatrix@Point


#pour donner les caractéristiques d'un pixel à savoir ses coordonnées dans un repère x,y et la couleur car on récupère une matrice en chargeant l'image
def givePixelCoordonate(image,dimension):
    imageAux=list(image)
    imageWithCoordonates=[]
    for k in range(0,len(imageAux)):
        coordonate=(k//dimension,k%dimension,imageAux[k])
        imageWithCoordonates.append(coordonate)
    return coordonate

#fonction principale donnant la couleur d'un pixel a la position x,y
def rotatePixelTrueColor(image,dimension,x,y):
        color=255
        imageWithCoordonates=givePixelCoordonate(image,dimension)
        for k in range(0,len(imageWithCoordonates)):
                if(imageWithCoordonates[k][0]==x and imageWithCoordonates[k][1]==y):
                    color=imageWithCoordonates[k][2]

        if (color==0):
            print("Pixel non trouvé, valeur par défaut")
        return color



#pour générer mes propres images test
def createImageTest(dimension):
    firstPixel=random.randint(0,255)
    img_numpy=np.full((1,dimension),firstPixel)

    for i in range(0,dimension):
        firstPixel=random.randint(0,255)
        new_img_numpy=np.full((1,dimension),firstPixel)
        img_numpy=np.concatenate((img_numpy,new_img_numpy))
    plt.imshow(img_numpy)
    plt.show()







#print(giveRotationMatrix(90))
print(createImageTest(4))
