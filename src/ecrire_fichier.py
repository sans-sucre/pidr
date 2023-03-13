import csv
import azi_scrapper


def traitement_data(data: str) -> list[tuple[float, float]]:
    """Cette fonction prend data sous forme string comme entrée et donne une liste de string comme sortie. Les données
    sorties ne comprisent que les azimuths et les hauteurs.
    @param data : Ce sont les données récupérées depuis internet type : string
    """
    azimuth_hauteur = []

    data_list = data.split('\n')
    for i in range(4, len(data_list)):
        element = data_list[i].split(" ")
        element[1] = transformer_str2float(element[1])
        element[2] = transformer_str2float(element[2])

        azimuth_hauteur.append((element[1], element[2]))
    return azimuth_hauteur


def transformer_str2float(ent: str) -> float:
    """Cette fonction permet de transformer une chaîne de caractère en int en enlevant le degré à la fin de la chaîne
    de caractères.
    @param ent: C'est une entrée sous forme de chaîne de caractère"""

    taille = len(ent)

    # c'est pour enlever le degré à la fin de la chaîne de caractères
    nouvel_float = float(ent[0:taille - 1])
    return nouvel_float


def export_data(data: list[tuple[float, float]]):
    """Cette fonction sert à écrire toutes les données dans le fichier csv"""
    ligne1 = ligne2 = []

    # séparer les données en deux listes, la première ligne présente azimuth, la deuxième est celle de hauteur
    for i in range(len(data)):
        ligne1.append(data[i][0])
        ligne2.append(data[i][1])

    # écrire les données dans le fichier csv, le fichier sorti s'appelle "data_web.csv"
    with open('../Data/data_web.csv', 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(ligne1)
        data_writer.writerow(ligne2)


# transformer les web data sous forme de liste de string, azi_scrapper est le programme utilisé pour récuréper
# des données
data_traite = traitement_data(azi_scrapper.data_web)
print(data_traite)

# exporter les données sous forme de csv
export_data(data_traite)
