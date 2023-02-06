import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

Image = Image.open( "Images/testImage.png" )
image_array = np.array( Image )
print( 'classe :', image_array) 
print( 'type :', image_array.dtype )
print( 'taille :', image_array.shape )
print( 'modifiable :', image_array.flags.writeable )