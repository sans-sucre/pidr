import array

import numpy as np
from PIL import Image


def ouvrir_image(chemin: str) -> Image:
    im = Image.open(chemin)
    im.show()
    return im


def rotation_image(image: Image, angle: float) -> Image:
    """Cette fonction permet de tourner une image en utilisant le module Image dans pillow, le paramètre image doit
     être une chaine de caractères"""
    im_rotation = image.rotate(angle)
    im_rotation.show()
    return im_rotation


def transformation_matrice(image: Image) -> array:
    """Cette fonction permet de transformer une image en une matrice (array)"""
    a = np.asarray(image)
    return a


def trouver_pixel(x: int, y: int, image: Image) -> array:
    """Cette fonction permet de récupérer la valeur d'un pixel avec une coordonnée donnée """
    pixel_rgb = np.asarray(image)
    return pixel_rgb[x][y]


def rotation_image_pixel(angle: float, chemin: str) -> array:
    """Cette fonction permet de tourner une image en transformant l'image en matrice"""
    image = ouvrir_image(chemin)
    image_rotation = rotation_image(image, angle)
    image_rotation_array = transformation_matrice(image_rotation)
    return image_rotation_array


def operation_array(matrice: array) -> array:
    """Cette fonction permet de tourner une image au niveau de matrice, qui permet de garder les valeurs qui peuvent
     être perdues pendant la rotation """


m = rotation_image_pixel(45, "../Images/testImage.png")
print(trouver_pixel(1000, 1500, m))
rotation_image(Image.fromarray(m), -45)
