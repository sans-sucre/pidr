import numpy as np


def coordonnes_polaire(x: float, y: float) -> tuple[float, float]:

    """
    Cette fonction sert à trouver les coordonnées polaires à partir de coordonnées cartésiennes
    """

    r = np.sqrt(x**2 + y**2)
    delta = np.arctan(y, x)
    return r, delta



def change_dimension(x: float, y: float) -> tuple[float, float, float]:

    """
    Cette fonction sert à retrouver les coordonnées dans 3 dimensions X,Y,Z à partir des x, y dans deux dimensions.
    """

    return X, Y, Z
