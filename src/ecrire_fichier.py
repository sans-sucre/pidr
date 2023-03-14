"""
Module qui contient les fonctions qui permettent de traiter les données récupérées
depuis internet et l'exporter dans un fichier 'data_web.csv'
"""
import csv

import azi_scrapper

HorizontalCoordinate = tuple[float, float]
DailySunTrajectory = list[HorizontalCoordinate]


def webdata_to_daily_sun_trajectory(webdata: str) -> DailySunTrajectory:
    """
    @param webdata: données récupérées depuis internet
    @return liste de couples azimuth/hauteur
    """
    azimuth_altitude_pairs = []

    webdata = webdata.split("\n")
    # les 4 premières lignes ne contiennent pas les données azimuth/hauteur
    webdata = webdata[4:]

    for azimuth_altitude_pair in webdata:
        _, azimuth_str, altitude_str, *_ = azimuth_altitude_pair.split(" ")
        azimuth = _degree_str_to_float(azimuth_str)
        altitude = _degree_str_to_float(altitude_str)
        azimuth_altitude_pairs.append((azimuth, altitude))

    return azimuth_altitude_pairs


def _degree_str_to_float(to_convert: str) -> float:
    """
    @param to_convert: élément à convertir vers un float en enlevant le symbole de
        degré à la fin.
    """
    to_convert = to_convert.removesuffix("°")
    return float(to_convert)


def export_daily_sun_trajectory_to_csv(
    daily_sun_trajectory: DailySunTrajectory,
) -> None:
    """Exporte la trajectoire du soleil dans un fichier au format csv."""
    azimuths = [azimuth for azimuth, _ in daily_sun_trajectory]
    altitudes = [altitude for _, altitude in daily_sun_trajectory]

    # écrire les données dans le fichier csv, le fichier sorti s'appelle "data_web.csv"
    with open("../Data/data_web.csv", "w", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(azimuths)
        writer.writerow(altitudes)


# transformer les web data sous forme de liste de string
# azi_scrapper est le programme utilisé pour récupérer des données
data_traite = webdata_to_daily_sun_trajectory(azi_scrapper.data_web)
print(data_traite)

# exporter les données sous forme de csv
export_daily_sun_trajectory_to_csv(data_traite)
