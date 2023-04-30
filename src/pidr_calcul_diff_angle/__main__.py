"""Interface utilisateur"""
import click
import statistique
import azi_scrapper as scrap
import ecrire_fichier as ecrire
import afficher_courbes as afficher


@click.command(help="Récupérer des données via SunEarthTools")
@click.option("-i", default=5, help="Interval entre deux données,"" valeur en minutes parmi 5,10,15,20,30,60")
@click.option("-a", default=1, help="Année de donnée à récupérer via SunEarthTools, 1970-2050")
@click.option("-m", default=1, help="Mois de donnée à récupérer via SunEarthTools, 1-12")
@click.option("-j", default=1, help="Jour de donnée à récupérer via SunEarthTools, 1-31")
def scrapper(i, a, m, j) -> None:
    data_web = scrap.execute(i, a, m, j)
    # transformer les web data sous forme de liste de string
    data_traite = ecrire.webdata_to_daily_sun_trajectory(data_web)
    # exporter les données sous forme de csv
    ecrire.export_daily_sun_trajectory_to_csv(data_traite)
    # afficher courbe
    afficher.afficher_courbes_ref("Data/data_web.csv")
    afficher.afficher_courbes_mes("Data/data_mes.csv")

    afficher.afficher_parcours("Data/data_web.csv", "Data/data_mes.csv")

    # vérifie si la modélisation est correcte enn affichant l'erreur moyenne sur les valeurs d'azimut et de hauteur

    statistique.modelisation_correcte("Data/data_web.csv", "Data/data_ref.csv", 0.5)
    # calcul le décalage d'azimut entre le fichier de reference et celui de mesure
    statistique.donne_moyenne_decalage_azimut_corrige("Data/data_ref.csv", "Data/data_mes.csv", 0.8)


if __name__ == '__main__':
    scrapper()
