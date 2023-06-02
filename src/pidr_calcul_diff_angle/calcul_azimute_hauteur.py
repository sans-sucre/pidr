import numpy as np


def matrice_rotation_z(rz: float):
    """Cette fonction sert à générer une matrice de rotation par rapport à l'axe z."""
    rz = np.deg2rad(rz)

    matrice_rotation = [[np.cos(rz), -np.sin(rz), 0, 0],
                        [np.sin(rz), np.cos(rz), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]]
    return matrice_rotation


def coordonnes_polaire(x: float, y: float) -> tuple[float, float]:
    """
    Cette fonction sert à trouver les coordonnées polaires à partir de coordonnées cartésiennes
    """

    assert (x != 0 or y != 0), "Attention, x et y ne peuvent pas être égaux à 0 en même temps"

    r = np.sqrt(x ** 2 + y ** 2)

    if x == 0 and y > 0:
        delta = -90
    elif x == 0 and y < 0:
        delta = 90
    else:
        delta = np.rad2deg(np.arctan(y / x))

    if x > 0 > y:
        delta += 180
    elif x > 0 and y > 0:
        delta -= 180

    return r, delta


def calcul_azimut_hauteur(x: float, y: float, z: float) -> tuple[float, float]:
    """
    Cette fonction sert à calculer l'azimute et la hauteur à partir de coordonnées cartésiennes du soleil données.
    L'abscisse doit être le nord magnétique, le point origine doit être le centre d'image. Les paramètres x et y sont
    en mm.
    """
    mr = matrice_rotation_z(90)
    matrice_coordonnes = np.multiply(np.array(mr), np.array([x, y, z, 1]))
    x = matrice_coordonnes[0][1]
    y = matrice_coordonnes[1][0]

    r, delta = coordonnes_polaire(x, y)
    azimut = delta
    f = 512 * np.sqrt(2)
    hauteur = (1 - r / f) * 90

    return azimut, hauteur

# a, h = calcul_azimut_hauteur(512, 512, 0)
# print(np.rad2deg(np.arctan(-1/(1))))
