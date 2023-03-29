import numpy as np
from math import *

def calculAzimutHauteur(x,y,z):
    rn=90
    xm = 512
    ym = 512
    zm=0
    rfov = 512*np.sqrt(2)
    rx = 0
    rz = 90
    tx = xm
    ty = ym
    tz = zm
    ry=0
    pix_xyz =np.array([[x, y,z]])
    Mrx = np.array([[1, 0, 0 ,0 ],[0,cos(0),-sin(0),0 ], [0, sin(0), cos(0) ,0 ], [0, 0, 0, 1]])
    Mry=np.array([[cos(0), 0, sin(0),0 ],[0,1,0,0], [-sin(0),0,cos(0),0 ], [0, 0, 0, 1]])
    Mrz=np.array([[cos(90),-sin(90),0,0 ],[sin(90),cos(90),0,0], [0,0,1,0 ], [0, 0, 0, 1]])
    Mtxyz=np.array([[1,0,0,-tx],[0,1,0,-ty],[0,0,1,-tz],[0,0,0,1]])
    tmp = np.array([[x, y,z,1]])
    pix_xyzc = np.matmul(tmp,Mtxyz)
    pix_xyzcr = np.matmul(pix_xyzc,Mrz)
    pix_xyzcr=pix_xyzcr[0]

    r = sqrt(pix_xyzcr[0]**2+pix_xyzcr[1]**2)
    a= atan(pix_xyzcr[1]/pix_xyzcr[0])*180/pi
    az = a
    gh = 1
    h = (1- r/rfov) * 90 *gh
    if (h<0):
        h=-1
        az=-1
        return az,h
    if (az<0):
        return 360+az,h
    
    return az,h
	

#bug ici
  

print(calculAzimutHauteur(1049,1785,0))
	
