# Pidr_callibration_2023

Développement d’un système de calibration automatisé hauteur-azimut en fonction de la position solaire à partir d’une caméra équipée d’un objectif à champ de vision hémisphérique connectée à un Raspberry PI B4.

## Table des matières

<!-- TOC -->
* [Pidr_callibration_2023](#pidrcallibration2023)
  * [Table des matières](#table-des-matières)
  * [Éditeurs](#éditeurs)
  * [Fonctionnalités](#fonctionnalités)
  * [Prérequis](#prérequis)
  * [Installation](#installation)
  * [Usage/Examples](#usageexamples)
      * [Instructions générales :](#instructions-générales--)
      * [Récupération des données depuis SunEarthTools :](#récupération-des-données-depuis-sunearthtools--)
      * [Visualisation des données :](#visualisation-des-données--)
      * [Obtentiion du décalage :](#obtentiion-du-décalage--)
  * [Pour plus d'information](#pour-plus-dinformation-)
<!-- TOC -->


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
Pour exécuter et obtenir la valeur du décalage sans correction sur les valeurs aberrantes :

```bash
python3 src/pidr_calcul_diff_angle/statistique.py -decalage nomDuFichierDeReference  nomDuFichierDeMesure
```
nomDuFichierDeReference : son chemin à partir du parcours relatif du fichier pidr 
nomDuFichierDeMesure : son chemin à partir du parcours relatif du fichier pidr 


Pour exécuter et obtenir la valeur du décalage avec une correction :

```bash
python3 src/pidr_calcul_diff_angle/statistique.py -decalage nomDuFichierDeReference  nomDuFichierDeMesure -correction  EMA
```
nomDuFichierDeReference : son chemin à partir du parcours relatif du fichier pidr 
nomDuFichierDeMesure : son chemin à partir du parcours relatif du fichier pidr 
EMA: valeur de l'erreur moyenne absolue pour supprimer de points


## Vérifier la concordance entre modélisation et valeurs réelles

Pour exécuter et obtenir l'ecart moyen en fixant la valeur du seuil
```bash
python3 python3 src/pidr_calcul_diff_angle/statistique.py -modelisation  nomDuFichierDeReference nomDuFichierDeMesure  -niveau Seuil
```
nomDuFichierDeReference : son chemin à partir du parcours relatif du fichier pidr 
nomDuFichierDeMesure : son chemin à partir du parcours relatif du fichier pidr 
Seuil: Le niveau seuil pour valider ou invalider la justesse de la modélisation


## Pour plus d'information 

 - [Module Selenium](https://selenium-python.readthedocs.io/installation.html)

 - [Site Web SunEarthTools ](https://www.sunearthtools.com/)

 - [Système de Coordonnées astronomiques](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_c%C3%A9lestes)

 - [Système de Coordonnées horizontales](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_horizontales)