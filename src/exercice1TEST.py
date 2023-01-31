import numpy as np
from PIL import Image

def cartToPol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def polToCart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def cartToGPS(x, y):
    a = np.arctan(x/y)
    e = e
    return(a, e)

def newCoord (transX,transY,rotD,x,y):
    x+=transX
    y+=transY
    x=np.cos(rotD)*x-np.sin(rotD)*x
    y=np.cos(rotD)*y+np.sin(rotD)*y
    return int(x), int(y)

def oldCoord (transX,transY,rotD,x,y):
    x-=transX
    y-=transY
    x=np.sin(rotD)*x-np.cos(rotD)*x
    y=-np.cos(rotD)*y-np.sin(rotD)*y
    return int(x), int(y)

def saveNewPicture (picName,transX,transY,rotD) :
    im = Image.open(picName) # Doit etre une string
    picture = im.load()

    imNew = Image.new(mode = "RGB", size = (2048, 2048), color = (255, 255, 255))
    pictureNew = imNew.load()

    for x in range (2048) :
        for y in range (2048) :
            xn, yn = oldCoord(x,y)
            value = picture[xn,yn]      # Get the RGBA Value of the a pixel of an image
            pictureNew[x,y] = value        # Set the RGBA Value of the image (tuple)

    imNew.save(picName)  # Save the modified pixels as .png
