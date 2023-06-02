"""Interface utilisateur"""
import click

import src.pidr_calcul_diff_angle.statistique as statistique
import src.pidr_calcul_diff_angle.azi_scrapper as scrap
import src.pidr_calcul_diff_angle.ecrire_fichier as ecrire
import src.pidr_calcul_diff_angle.afficher_courbes as afficher


@click.group()
def calibration():
    pass


@calibration.command(help="Récupérer des données via SunEarthTools")
@click.option("-a", default=2023, help="Année de donnée à récupérer via SunEarthTools, 1970-2050")
@click.option("-m", default=1, help="Mois de donnée à récupérer via SunEarthTools, 1-12")
@click.option("-j", default=1, help="Jour de donnée à récupérer via SunEarthTools, 1-31")
def scrapper(a, m, j) -> None:
    data_web = scrap.execute(5, a, m, j)
    # transformer les web data sous forme de liste de string
    data_traite = ecrire.webdata_to_daily_sun_trajectory(data_web)
    # exporter les données sous forme de csv
    ecrire.export_daily_sun_trajectory_to_csv(data_traite)
    click.echo("Les données récupérées sont enregistrées dans Data/data_web.csv")


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
    click.echo("Les courbes sont enregistrées dans répertoire Images")


@calibration.command(help="Vérifier si la modélisation est correcte en affichant "
                          "l'erreur moyenne sur les valeurs d'azimut et de hauteur")
@click.option("-ref", default="Data/data_web.csv", help="Fichier de données de référence.")
@click.option("-mes", default="Data/data_ref.csv", help="Fichier de données à comparer.")
@click.option("-n", default=1.0, help="Seuil pour valider ou non la modélisation par défaut, sa valeur est 1")
def check(ref, mes, n) -> None:
    # vérifie si la modélisation est correcte en affichant l'erreur moyenne sur les valeurs d'azimut et de hauteur
    msg = statistique.modelisation_correcte(ref, mes, n)
    click.echo(msg)


@calibration.command(help="Calculer le décalage d'azimut entre le fichier de reference et celui de mesure")
@click.option("-ref", default="Data/data_ref.csv", help="Fichier de référence.")
@click.option("-mes", default="Data/data_mes.csv", help="Fichier de données mesurées.")
@click.option("-s", default=200.0, help="Valeur d'erreur quadratique moyenne pour "
                                      "corriger les données, si elle n'est pas renseignée il n'y a pas de correction")
def decalage(ref, mes, s) -> None:
    # calcul le décalage d'azimut entre le fichier de reference et celui de mesure
    _v1 = statistique.donne_moyenne_decalage_azimut_corrige(ref, mes, s)
    click.echo(f"Décalage d'azimut : {_v1}")


@calibration.command(help="Exécuter l'ensemble des fonctions")
@click.option("-a", default=2023, help="Année de donnée à récupérer via SunEarthTools, 1970-2050")
@click.option("-m", default=1, help="Mois de donnée à récupérer via SunEarthTools, 1-12")
@click.option("-j", default=1, help="Jour de donnée à récupérer via SunEarthTools, 1-31")
@click.option("-n", default=0.5, help="Niveau de correction, par défaut, sa valeur est 0.5")
@click.option("-s", default=0.8, help="Seuil de modélisation, par défaut, sa valeur est 0.8")
def tout(a, m, j, n, s) -> None:
    data_web = scrap.execute(5, a, m, j)
    # transformer les web data sous forme de liste de string
    data_traite = ecrire.webdata_to_daily_sun_trajectory(data_web)
    # exporter les données sous forme de csv
    ecrire.export_daily_sun_trajectory_to_csv(data_traite)

    # vérifie si la modélisation est correcte en affichant l'erreur moyenne sur les valeurs d'azimut et de hauteur

    msg = statistique.modelisation_correcte("Data/data_web.csv", "Data/data_ref.csv", n)
    click.echo(msg)
    # calcul le décalage d'azimut entre le fichier de reference et celui de mesure
    _v1 = statistique.donne_moyenne_decalage_azimut_corrige("Data/data_ref.csv", "Data/data_mes.csv", s)
    click.echo(f"Décalage d'azimut conseillé : {_v1}")


if __name__ == '__main__':
    calibration()
