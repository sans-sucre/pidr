import array

import numpy as np
from PIL import Image


def calcul_coordonne_rotation(x: float, y: float, angle_rotation: float) -> tuple[float, float]:
    """Cette fonction sert à calculer les coordonnées après la rotation de certain angle, le paramètre angle_rotation
     est d'unité degré"""

    angle_rotation = np.deg2rad(angle_rotation)
    matrice_rotation = np.array([[np.cos(angle_rotation), (-1) * np.sin(angle_rotation)],
                                 [np.sin(angle_rotation), np.cos(angle_rotation)]])
    x, y = calcul_coordonne_translation(x, y, -1023.5, -1023.5)
    r = np.matmul(matrice_rotation, np.array([x, y]))
    return int(np.rint(r[0] + 1023.5)), int(np.rint(r[1] + 1023.5))


def calcul_coordonne_translation(x: float, y: float, x_translation: float, y_translation: float) -> tuple[float, float]:
    """Cette fonction sert à calculer les coordonnées après la translation"""

    return x + x_translation, y + y_translation


def ouvrir_image(chemin: str) -> Image:

    im = Image.open(chemin)
    im = im.resize((2048, 2048))
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
    image_rotation = rotation_image(image, (-1) * angle)
    image_rotation_array = transformation_matrice(image_rotation)
    return image_rotation_array


def rotation_array(matrice: array, angle: float) -> array:
    """Cette fonction permet de tourner la matrice d'une image après la rotation"""
    new_image = Image.new("RGB", [2048, 2048])
    matrice_taille = np.shape(matrice)
    nb_ligne = matrice_taille[0]
    nb_colonne = matrice_taille[1]

    for i in range(nb_ligne):
        for j in range(nb_colonne):
            x_rotation, y_rotation = calcul_coordonne_rotation(i, j, angle)
            if 0 <= x_rotation < 2048 and 0 <= y_rotation < 2048:
                new_image.putpixel((j, i), tuple(matrice[x_rotation][y_rotation]))
    new_image.show()


m = rotation_image_pixel(100, "../Images/testImage2.png")
m2 = rotation_image_pixel(0, "../Images/testImage2.png")
rotation_array(m2, 100)
