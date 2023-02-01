import numpy as np


def coordonnes_polaire(x: float, y: float) -> tuple[float, float]:
    """
    Cette fonction sert à trouver les coordonnées polaires à partir de coordonnées cartésiennes
    """

    assert (x != 0 or y != 0), "Attention, x et y ne peuvent pas être égaux à 0 en même temps"
    r = np.sqrt(x ** 2 + y ** 2)

    if x == 0 and y > 0:
        delta = 90
    elif x == 0 and y < 0:
        delta = 270
    else:
        delta = np.rad2deg(np.arctan(y / x))

    if x < 0 < y:
        delta += 90
    elif x < 0 and y < 0:
        delta += 180
    elif x > 0 > y:
        delta += 270

    return r, delta


def calcul_azimut_hauteur(x: float, y: float) -> tuple[float, float]:
    """
    Cette fonction sert à calculer l'azimute et la hauteur à partir de coordonnées cartésiennes du soleil données.
    L'abscisse doit être le nord magnétique, le point origine doit être le centre d'image. Les paramètres x et y sont
    en mm.
    """

    r, delta = coordonnes_polaire(x, y)
    azimut = delta
    print("rayon :", r)
    f = 2.7
    hauteur = 90 - np.rad2deg(r/f)
    print("hauteur :", hauteur)
    return azimut, hauteur


a, h = calcul_azimut_hauteur(0.5, 0.5)
print(a, h)
