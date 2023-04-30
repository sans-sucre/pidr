import unittest
import numpy as np

import src.calcul_azimute_hauteur as calcul


class TestCalculAzimutHauteur(unittest.TestCase):

    def test_matrix_rotation_z(self):
        _m_0 = calcul.matrice_rotation_z(0)
        self.assertEqual(_m_0, [[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])
        _m_1 = calcul.matrice_rotation_z(180)

        self.assertEqual(_m_1, [[-1, -1.2246467991473532e-16, 0, 0],
                                [1.2246467991473532e-16, -1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

        _m_2 = calcul.matrice_rotation_z(90)
        self.assertEqual(_m_2, [[6.123233995736766e-17, -1.0, 0, 0],
                                [1.0, 6.123233995736766e-17, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

    def test_azimut_hauteur(self):
        _value_0 = calcul.calcul_azimut_hauteur(150, 150, 0)

        self.assertEqual(_value_0, (-45.0, 63.6328125))

        _value_1 = calcul.calcul_azimut_hauteur(90, 45, 0)
        self.assertEqual(_value_1, (-63.43494882292201, 77.49294480109185))

        _value_2 = calcul.calcul_azimut_hauteur(100, 200, 0)
        self.assertEqual(_value_2, (-26.56505117707799, 62.206544002426355))
