"""Interface utilisateur"""
import click
import statistique
import src.pidr_calcul_diff_angle.azi_scrapper as scrap
import src.pidr_calcul_diff_angle.ecrire_fichier as ecrire
import src.pidr_calcul_diff_angle.afficher_courbes as afficher


@click.group()
def calibration():
    pass


@calibration.command(help="Récupérer des données via SunEarthTools")
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

    # vérifie si la modélisation est correcte en affichant l'erreur moyenne sur les valeurs d'azimut et de hauteur

    statistique.modelisation_correcte("Data/data_web.csv", "Data/data_ref.csv", 0.5)
    # calcul le décalage d'azimut entre le fichier de reference et celui de mesure
    statistique.donne_moyenne_decalage_azimut_corrige("Data/data_ref.csv", "Data/data_mes.csv", 0.8)


@calibration.command(help="Visualiser les données (afficher les courbes des données), les données à visualiser doivent"
                          " être déposées dans le dossier Data sous format csv, le fichier doit contenir 288 couple de"
                          "valeurs, format cf Data/data_ref.csv. Les résultats vont être enregistrés dans dossier "
                          "Images du projet")
@click.option("-ref", default="Data/data_web.csv", help="Afficher la courbe des données théoriques.")
@click.option("-mes", default="Data/data_mes.csv", help="Afficher la courbe des données mesurées.")
def courbe(ref, mes) -> None:
    # afficher courbe
    afficher.afficher_courbes_ref(ref)
    afficher.afficher_courbes_mes(mes)
    afficher.afficher_parcours("Data/data_web.csv", "Data/data_mes.csv")


@calibration.command(help="Vérifier si la modélisation est correcte en affichant "
                          "l'erreur moyenne sur les valeurs d'azimut et de hauteur")
@click.option("-ref", default="Data/data_web.csv", help="Afficher la courbe des données théoriques.")
@click.option("-mes", default="Data/data_mes.csv", help="Afficher la courbe des données mesurées.")
@click.option("-n", default=0.5, help="Niveau de correction, par défaut, sa valeur est 0.5")
def check(ref, mes) -> None:
    # vérifie si la modélisation est correcte en affichant l'erreur moyenne sur les valeurs d'azimut et de hauteur
    statistique.modelisation_correcte(ref, mes, 0.5)


@calibration.command(help="Calculer le décalage d'azimut entre le fichier de reference et celui de mesure")
@click.option("-ref", default="Data/data_web.csv", help="Afficher la courbe des données théoriques.")
@click.option("-mes", default="Data/data_mes.csv", help="Afficher la courbe des données mesurées.")
@click.option("-s", default=0.8, help="Seuil de modélisation, par défaut, sa valeur est 0.8")
def decalage(ref, mes) -> None:
    # calcul le décalage d'azimut entre le fichier de reference et celui de mesure
    statistique.donne_moyenne_decalage_azimut_corrige(ref, mes, 0.8)


@calibration.command(help="Exécuter l'ensemble des fonctions")
@click.option("-i", default=5, help="Interval entre deux données,"" valeur en minutes parmi 5,10,15,20,30,60")
@click.option("-a", default=1, help="Année de donnée à récupérer via SunEarthTools, 1970-2050")
@click.option("-m", default=1, help="Mois de donnée à récupérer via SunEarthTools, 1-12")
@click.option("-j", default=1, help="Jour de donnée à récupérer via SunEarthTools, 1-31")
@click.option("-n", default=0.5, help="Niveau de correction, par défaut, sa valeur est 0.5")
@click.option("-s", default=0.8, help="Seuil de modélisation, par défaut, sa valeur est 0.8")
def tout(i, a, m, j, n, s) -> None:
    data_web = scrap.execute(i, a, m, j)
    # transformer les web data sous forme de liste de string
    data_traite = ecrire.webdata_to_daily_sun_trajectory(data_web)
    # exporter les données sous forme de csv
    ecrire.export_daily_sun_trajectory_to_csv(data_traite)

    # vérifie si la modélisation est correcte en affichant l'erreur moyenne sur les valeurs d'azimut et de hauteur

    statistique.modelisation_correcte("Data/data_web.csv", "Data/data_ref.csv", n)
    # calcul le décalage d'azimut entre le fichier de reference et celui de mesure
    statistique.donne_moyenne_decalage_azimut_corrige("Data/data_ref.csv", "Data/data_mes.csv", s)


if __name__ == '__main__':
    calibration()
