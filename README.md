# Pidr_callibration_2023

Développement d’un système de calibration automatisé hauteur-azimut en fonction de la position solaire à partir d’une caméra équipée d’un objectif à champ de vision hémisphérique connectée à un Raspberry PI B4.


## Éditeurs

- [@Cloée Hareau](Cloee.Hareau@telecomnancy.eu)
- [@Ndeye-Emilie Mbengue](Ndeye.Mbengue@telecomnancy.eu)
- [@Wenjia Tang](Wenjia.Tang@telecomnancy.eu)


## Fonctionnalités

- Récupération automatique des données d'azimutes et de hauteurs depuis siteweb [SunEarthTools](https://www.sunearthtools.com/).
- Visualisation des données récupérées depuis caméra posée à Apheen et celles de [SunEarthTools](https://www.sunearthtools.com/).
- Vérification des données récupérées depuis la caméra en se référeant à celles de  [SunEarthTools](https://www.sunearthtools.com/).
- Calculs de la différence d'azimuth entre la valeur théorique (relevée depuis website [SunEarthTools](https://www.sunearthtools.com/)) et la valeur mesurée par la caméra.


## Prérequis
Pour assurer le bon fonctionnement du projet, il faut avoir python de version 3.10, le module Selenium, et le navigateur Chrome installés sur votre machine.

**Python3.10:**

https://www.python.org/downloads/release/python-3100/


**selenium:** 
```bash
pip install selenium
```

**numpy:**
```bash
pip install numpy
```

**matplotlib:**
```bash
python -m pip install -U pip
python -m pip install -U matplotlib
```

**csv:**
```bash
pip install python-csv
```

## Installation

Cloner notre projet depuis github :
```bash
git clone https://gitlab.telecomnancy.univ-lorraine.fr/Wenjia.Tang/pidr.git
```

## Usage/Examples

####  Instructions générales : 
```bash
cd src
python3 nom_programme.py 
```
#### Récupération des données depuis SunEarthTools : 
- Pour se déplacer dans le répertoire src : 
```bash
cd src
```
- Pour relever des données : 
```bash
python3 azi_scrapper.py interval année mois date
```
Ici la valeur d'interval peut être 5,10,15,20,30,60
- Pour relever et exporter les données sous forme de fichier csv : 
```bash
python3 ecrire_fichier.py 
```
#### Visualisation des données : 

- Pour visualiser les données il faut être dans le repertoire pidr. Si vous êtes dans le répertoire src, faites : 
```bash
cd ..
```
- Pour enregistrer les courbes : 
```bash
python3 affichercourbes.py nomDuFichierDeReference nomDuFichierDeMesure
```
nomDuFichierDeReference : son chemin à partir du parcours relatif du fichier pidr 
nomDuFichierDeMesure : son chemin à partir du parcours relatif du fichier pidr 

#### Obtentiion du décalage : 
Pour exécuter et obtenir la valeur du décalage :

```bash
python3 src/statistique.py nomDuFichierDeReference nomDuFichierDeMesure
```
nomDuFichierDeReference : son chemin à partir du parcours relatif du fichier pidr 
nomDuFichierDeMesure : son chemin à partir du parcours relatif du fichier pidr 


## Pour plus d'information 

 - [Module Selenium](https://selenium-python.readthedocs.io/installation.html)

 - [Site Web SunEarthTools ](https://www.sunearthtools.com/)

 - [Système de Coordonnées astronomiques](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_c%C3%A9lestes)

 - [Système de Coordonnées horizontales](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_horizontales)