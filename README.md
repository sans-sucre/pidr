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
Pour assurer le bon fonctionnement du projet, il faut avoir python de version supérieure à 3.10, également gestionnaire de packages pour Python "pip".

**Python3.10:**

https://www.python.org/downloads/release/python-3100/

## Installation

Cloner notre projet depuis github :
```bash
git clone https://gitlab.telecomnancy.univ-lorraine.fr/Wenjia.Tang/pidr.git
```
###  Configuration d'environnement virtuel


Pour installer notre projet sans interférer avec les packages déjà installés globalement, il est conseillé d'utiliser un environnement virtuel :
 1) Ouvrez un terminal ou une invite de commande.
 2) Naviguez vers le dossier racine de votre projet.
 3) Créez un nouvel environnement virtuel en exécutant la commande suivante :
    ```bash
    python3 -m venv env
    ```
 4) Activez l'environnement virtuel en exécutant la commande suivante :
    
    Sur Linux/Mac :  
    ```bash
    source env/bin/activate
    ```
    Sur Windows :
    ```bash
    env\Scripts\activate.bat
    ```
 5) Vous pouvez maintenant installer les packages à notre projet dans cet environnement virtuel à l'aide de pip.
 ### Installation des packages nécessaires
Pour installer les packages nécessaires pour exécuter notre projet, il vous faut exécuter la ligne de commande suivante sur votre terminal : 
  ```bash
  pip install -e .
  ```

## Usage/Examples

####  Instructions générales :
Pour exécuter le projet dans votre terminal, vous pouvez exécuter : 
```bash
python src/pidr_calcul_diff_angle -a $(ANNEE) -m $(MOIS) -j $(JOUR) 
```
$(ANNEE)  $(MOIS) et $(JOUR) sont à remplacer par les valeurs correspondantes, ils signifient le jour (l'année, le mois et le jour) duquel les données théoriques (les valeurs d'azimut et de hauteur) à récupérer depuis [SunEarthTools]((https://www.sunearthtools.com/))   
Les courbes : todo blabla



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


### Vérifier la concordance entre modélisation et valeurs réelles

Pour exécuter et obtenir l'ecart moyen en fixant la valeur du seuil
```bash
python3 python3 src/pidr_calcul_diff_angle/statistique.py -modelisation  nomDuFichierDeReference nomDuFichierDeMesure  -niveau Seuil
```
nomDuFichierDeReference : son chemin à partir du parcours relatif du fichier pidr 
nomDuFichierDeMesure : son chemin à partir du parcours relatif du fichier pidr 
Seuil: Le niveau seuil pour valider ou invalider la justesse de la modélisation

### Help
Pour avoir plus d'informations concernant aux lignes de commandes, vous pouvez utiliser help :
```bash
python src/pidr_calcul_diff_angle --help
```

## Tests
Des tests unitaires sont également à votre disposition, pour exécuter les tests, il faut tout simplement exécuter la ligne de commande suivante :
```bash
pytest
```

## Pour plus d'information 

 - [Module Selenium](https://selenium-python.readthedocs.io/installation.html)

 - [Site Web SunEarthTools ](https://www.sunearthtools.com/)

 - [Système de Coordonnées astronomiques](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_c%C3%A9lestes)

 - [Système de Coordonnées horizontales](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_horizontales)