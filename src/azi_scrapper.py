"""
Module qui contient tous les programmes qui permettent de récupérer les données
depuis internet en utilisant module selenium.
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# configuration des options de webdriver
options = webdriver.ChromeOptions()
options.add_argument("-headless")
options.add_argument("-no-sandbox")
options.add_argument("-disable-dev-shm-usage")

driver = webdriver.Chrome("chromedriver", options=options)
driver.get("https://www.sunearthtools.com/dp/tools/pos_sun.php?lang=fr")

sleep(1)


def config_interval(interval: int) -> None:
    """
    Configure les intervalles de mesure. Par défaut, l'intervalle est de 60 minutes.

    @param interval : valeur en minutes parmi 5,10,15,20,30,60
    """
    _select_x('//*[@id="step"]', interval)
    submit = driver.find_element(By.XPATH, '//*[@id="formStep"]/input')
    submit.click()


def config_date(
    annee: int | None,
    mois: int | None,
    jour: int | None,
    heure: int | None,
    minute: int | None,
) -> None:
    """
    Sélectionne la date des données à récupérer. Par défaut, l'heure courante.

    @param annee: 1970-2050
    @param mois: 1-12
    @param jour: 1-31
    @param heure: 0-23
    @param minute: 0-59
    """
    param_xpath_pairs = [
        (annee, '//*[@id="year"]'),
        (mois, '//*[@id="month"]'),
        (jour, '//*[@id="day"]'),
        (heure, '//*[@id="hour"]'),
        (minute, '//*[@id="minute"]'),
    ]

    for param, xpath in param_xpath_pairs:
        if param:
            _select_x(xpath, param)

    submit = driver.find_element(
        By.XPATH, '//*[@id="formE"]/table/tbody/tr[5]/td[3]/input'
    )
    submit.click()


def _select_x(xpath: str, valeur: int) -> None:
    """
    @param xpath : select dont le contenu doit être rempli
    @param valeur : valeur à sélectionner
    """
    select = Select(driver.find_element(By.XPATH, xpath))
    select.select_by_value(str(valeur))
    print(select.first_selected_option.text)


# configuration de date de données à récupérer, None = valeur par défaut, cf config_date
# exemple : config_date(2023, 2, 25, 12, 24) : 25 fev 2023 à 12 h 24
sleep(1)

# configuration d'intervalle de données à récupérer, None = intervalle = 60 mins
config_interval(5)

sleep(1)
# Configuration des coordonnées, les coordonnées d'Apheen sont utilisées. Ne pas le modifiez.
coord = driver.find_element(By.XPATH, '//*[@id="findLoc"]')
coord.send_keys("48.6641764,6.1683365")
coord.send_keys(Keys.RETURN)

sleep(1)

# data sans traitement, pour l'exporter, rf ecrire_fichier.py
data_web = coord.find_element(By.XPATH, '//*[@id="tabSunHour"]').text
#print(data_web)
driver.close()
