"""Interface utilisateur"""
import click

import azi_scrapper as scrap
import ecrire_fichier as ecrire


@click.command(help="Récupérer des données via SunEarthTools")
@click.option("--interval", default=5, help="Interval entre deux données,"
                                            " valeur en minutes parmi 5,10,15,20,30,60")
@click.option("--an", default=1, help="Année de donnée à récupérer via SunEarthTools, 1970-2050")
@click.option("--mois", default=1, help="Mois de donnée à récupérer via SunEarthTools, 1-12")
@click.option("--jour", default=1, help="Jour de donnée à récupérer via SunEarthTools, 1-31")
def scrapper(interval, an, mois, jour) -> None:
    data_web = scrap.execute(interval, an, mois, jour)
    # transformer les web data sous forme de liste de string
    data_traite = ecrire.webdata_to_daily_sun_trajectory(data_web)
    # exporter les données sous forme de csv

    ecrire.export_daily_sun_trajectory_to_csv(data_traite)
    print("test")


if __name__ == '__main__':
    scrapper()




