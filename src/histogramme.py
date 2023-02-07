from typing import List

import matplotlib.pyplot as plt
import numpy as np


def lire_fichier(chemin: str) -> List[str]:
    """Cette fonction sert à ouvrir un fichier et lire un fichier"""
    with open(chemin, "r") as fichier:
        lignes = fichier.readlines()
        fichier.close()
    return lignes


def reformer_donnees(donnees) :
    """Cette fonction permet de reformer les données sous forme d'une liste constituée par des tuples. Le premier
    élément dans le tuple représente l'azimut, le deuxième représente la hauteur"""

    donnees_reforme = []
    for i in range(len(donnees)):
        ligne = donnees[i].strip().split(",")
        donnees_reforme.append([ligne[0], ligne[1]])
        print("1 : ", ligne[0], "2 : ", ligne[1])
    return donnees_reforme


def afficher_histogramme(data) :
    """Cette fonction sert à afficher un histogramme à partir d'une liste qui est constituée par des tuples."""
    liste_azimut = []
    liste_hauteur = []
    for i in range(len(data)):
        liste_azimut.append(float(data[i][0]))
        liste_hauteur.append(float(data[i][1]))

    counts, bins = np.histogram(np.array(liste_azimut), bins=np.arange(360), density='True')
    counts, bins = np.histogram(np.array(liste_azimut), bins=np.arange(360), density='True')
    
    plt.stairs(counts, bins)
    # print(counts, bins, np.array(liste_azimut))

    plt.grid(axis='y', alpha=0.5)
    plt.xlabel('Valeur')
    plt.ylabel('Fréquence')
    plt.title('Histogramme de données azimute')
    plt.text(23, 45, r'$\mu=15, b=3$')
    plt.show()


def histogramme_test():
    lines = lire_fichier("../Data/data.txt")
    data_test = reformer_donnees(lines)
    afficher_histogramme2(data_test)


#pour afficher la proportion des deux jeux de données dans deux figures et améliorer la visualisation
def afficher_histogramme2(data) :
    """Cette fonction sert à afficher un histogramme à partir d'une liste qui est constituée par des tuples."""
    liste_azimut = []
    liste_hauteur = []
    for i in range(len(data)):
        liste_azimut.append(float(data[i][0]))
        liste_hauteur.append(float(data[i][1]))
    plt.hist(liste_azimut, label='azimut', alpha=0.7, edgecolor='blue')
    plt.xlabel('Valeur')
    plt.ylabel('Fréquence')
    plt.title('Histogramme de données de l\'azimute')
    plt.grid(axis='y', alpha=0.5)
    plt.legend()
    plt.figure(2)

    plt.hist(liste_hauteur, label='hauteur', alpha=0.7, edgecolor='blue')
    plt.xlabel('Valeur')
    plt.ylabel('Fréquence')
    plt.title('Histogramme de données de la hauteur')
    plt.grid(axis='y', alpha=0.5)
    plt.legend()
    plt.show()


histogramme_test()