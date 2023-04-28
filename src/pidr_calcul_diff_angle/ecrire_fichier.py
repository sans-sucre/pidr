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
    time_data = []

    webdata = webdata.split("\n")
    # les 4 premières lignes ne contiennent pas les données azimuth/hauteur

    webdata = webdata[4:]

    for azimuth_altitude_pair in webdata:
        time_str, azimuth_str, altitude_str, *_ = azimuth_altitude_pair.split(" ")
        azimuth = _degree_str_to_float(azimuth_str)
        altitude = _degree_str_to_float(altitude_str)
        azimuth_altitude_pairs.append((azimuth, altitude))
        time_data.append(time_str)

    time_sunrise_str = time_data[1]
    time_sunset_str = time_data[-2]
    # print(time_sunrise_str, time_sunset_str)
    time_sunrise_minutes = _time_to_minute(time_sunrise_str)
    time_sunset_minutes = _time_to_minute(time_sunset_str)
    zero_padding_head = _zero_padding(time_sunrise_minutes-5)
    zero_padding_tail = _zero_padding(1440-time_sunset_minutes)
    azimuth_altitude_pairs = zero_padding_head + azimuth_altitude_pairs + zero_padding_tail
    # print(time_sunrise_minutes,time_sunset_minutes)
    print(len(azimuth_altitude_pairs))
    return azimuth_altitude_pairs


def _degree_str_to_float(to_convert: str) -> float:
    """
    @param to_convert: élément à convertir vers un float en enlevant le symbole de
        degré à la fin.
    """
    to_convert = to_convert.removesuffix("°")
    return float(to_convert)


def _zero_padding(interval_time: int) -> DailySunTrajectory:
    """
    @param interval_time: horaire en minute
    @return: liste de zéros
    """
    zero_padding = []
    number_padding = int(interval_time/5)
    for i in range(number_padding-1):
        zero_padding.append((0, 0))
    return zero_padding


def _time_to_minute(to_convert: str) -> int:
    """
    @param to_convert: une chaine de caractère qui présente horaire à convertir vers minute
    @return: nombre de minutes
    """
    to_converts = to_convert.split(":")
    minutes = int(to_converts[0])*60 + int(to_converts[1])
    return minutes



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
        writer.writerow(altitudes)
        writer.writerow(azimuths)


# transformer les web data sous forme de liste de string
# azi_scrapper est le programme utilisé pour récupérer des données
data_traite = webdata_to_daily_sun_trajectory(azi_scrapper.data_web)
print(data_traite)

# exporter les données sous forme de csv
export_daily_sun_trajectory_to_csv(data_traite)
