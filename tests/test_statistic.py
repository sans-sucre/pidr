import unittest
import numpy as np
import src.pidr_calcul_diff_angle.statistique as statistique


class TestCalculStatistique(unittest.TestCase):

    def test_erreur_moyenne_absolue(self):
        _v_0 = statistique.donne_erreur_moyenne_absolue([5, 3, 4, 12], [8, 4, 4, 10])
        self.assertEquals(_v_0, 0.275)

        _v_2 = statistique.donne_erreur_moyenne_absolue([4, 4, 4, 4], [4, 4, 4, 4])
        self.assertEquals(_v_2, 0)

    def test_decalage(self):
        _v_0 = statistique.donne_decalage(10, 30)
        self.assertEquals(_v_0, 20)

        _v_1 = statistique.donne_decalage(0, 0)
        self.assertEquals(_v_1, 0)
