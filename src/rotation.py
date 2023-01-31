import numpy as np

R = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])


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


def calcul_azimute_hauteur(x: float, y: float) -> tuple[float, float]:
    """
    Cette fonction sert à calculer l'azimute et la hauteur à partir de coordonnées cartésiennes du soleil données.
    L'abscisse doit être le nord magnétique, le point origine doit être le centre d'image .
    """

    r, delta = coordonnes_polaire(x, y)
    azimute = delta

    hauteur = 90 - np.rad2deg(np.arctan(r))
    return azimute, hauteur


def change_dimension(x: float, y: float) -> tuple[float, float, float]:
    """
    Cette fonction sert à retrouver les coordonnées dans 3 dimensions X,Y,Z à partir des x, y dans deux dimensions.
    """

    r, delta = coordonnes_polaire(x, y)
    theta = np.arctan(r)
    phi = np.arctan(y / x)
    M2 = np.array([[(np.cos(phi)) * np.sin(theta)],
                   [np.sin(phi) * np.sin(theta)],
                   [np.cos(theta)]])
    R_inverse = np.linalg.inv(R)

    M_resultat = np.multiply(R_inverse, M2)
    print(M_resultat)
    X = M_resultat[0]
    Y = M_resultat[1]
    Z = M_resultat[2]

    return X, Y, Z


a, h = calcul_azimute_hauteur(0, 0)
print(a, h)
# X,Y,Z=change_dimension(2000,1000)
# print(X,Y,Z)
