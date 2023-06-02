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
    * [Configuration d'environnement virtuel](#configuration-denvironnement-virtuel)
    * [Installation des packages nécessaires](#installation-des-packages-nécessaires)
  * [Usage/Examples](#usageexamples)
    * [Instructions générales](#instructions-générales-)
    * [Instructions de chaque module](#instructions-de-chaque-module-)
      * [Scrapper](#scrapper)
      * [Courbe](#courbe)
      * [Decalage](#decalage-)
      * [Check](#check)
    * [Help](#help)
  * [Tests](#tests)
  * [Pour plus d'information](#pour-plus-dinformations-)
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
 
**Note** : Pour quitter l'environnement virtuel, il faut utiliser 
  ```bash
  deactivate
  ```
    
    

## Usage/Examples

###  Instructions générales 
Pour exécuter le projet dans votre terminal depuis le répertoire racine du projet, vous pouvez exécuter : 
```bash
python src/pidr_calcul_diff_angle tout -a $(ANNEE) -m $(MOIS) -j $(JOUR) -n $(NIVEAU DE CORRECTION) -s $(SEUIL) 
```
$(ANNEE)  $(MOIS) $(JOUR) sont à remplacer par les valeurs correspondantes, ils signifient le jour (l'année, le mois et le jour) duquel les données théoriques (les valeurs d'azimut et de hauteur) à récupérer depuis [SunEarthTools]((https://www.sunearthtools.com/)). Par default, la date est 01/01/2023  
$(NIVEAU DE CORRECTION) est le niveau de correction, par default, sa valeur est égal à 0.5. $(SEUIL) représente la valeur de seuil de modélisation, sa valeur par default est 0.8. 

Après l'exécution de l'ensemble des programmes, vous pouvez avoir trois courbes apparues dans le répertoire Images. Il y a "azimutHauteurFichierMesures.png" qui représente les données mesurées, "azimutHauteurFichierRef.png" représente les données théoriques, qui sont récupérés depuis [SunEarthTools](https://www.sunearthtools.com/), et "parcoursSoleil.png" affiche le parcours du soleil.

Les valeurs d'erreurs sur l'azimut et sur la hauteur seront affichées sur le terminal, ainsi le résultat de la modélisation et le décalage d'azimut.

### Instructions de chaque module 

#### Scrapper
Pour récupérer des données depuis [SunEarthTools](https://www.sunearthtools.com/), vous pouvez utiliser la ligne de commande suivante : 
```bash
python src/pidr_calcul_diff_angle scrapper -a $(ANNEE) -m $(MOIS) -j $(JOUR)  
```
_Exemple_

Pour récupérer les données de 1/5/2023 : 
```bash
python src/pidr_calcul_diff_angle scrapper -a 2023 -m 5 -j 1  
```

#### Courbe
Pour visualiser les données (afficher les courbes des données), les données à visualiser doivent être déposées dans le dossier Data sous format csv, le fichier doit contenir 288 couple de valeurs, format cf. Data/data_ref.csv.
Vous pouvez utiliser la ligne de commande suivante pour exécuter : 

```bash
python src/pidr_calcul_diff_angle courbe -ref $(NOM_FICHIER_REFERENCE) -mes $(NOM_FICHIER_MESURE)
```
NOM_FICHIER_REFERENCE : son chemin à partir du parcours relatif du fichier pidr, par exemple, Data/data_ref 

NOM_FICHIER_MESURE : son chemin à partir du parcours relatif du fichier pidr, par exemple, Data/data_web

_Exemple_

```bash
python src/pidr_calcul_diff_angle courbe -ref Data/data_ref.csv  -mes Data/data_mes.csv 
```


#### Decalage 
Pour exécuter et obtenir la valeur du décalage sur les valeurs aberrantes :

```bash
python src/pidr_calcul_diff_angle decalage -ref $(NOM_FICHIER_REFERENCE) -mes $(NOM_FICHIER_MESURE) -s $(CORRECTION) 
```
NOM_FICHIER_REFERENCE : son chemin à partir du parcours relatif du fichier pidr, par exemple, Data/data_ref 

NOM_FICHIER_MESURE : son chemin à partir du parcours relatif du fichier pidr, par exemple, Data/data_web

CORRECTION : valeur d'erreur quadratique moyenne pour corriger les données, si elle n'est pas renseignée, il n'y a pas de correction


_Exemple_

```bash
python src/pidr_calcul_diff_angle decalage -ref Data/data_ref.csv  -mes Data/data_mes.csv -s 0.8
```

#### Check
Pour vérifier la concordance entre modélisation et valeurs réelles, vous pouvez exécuter avec la ligne de commande suivante et obtenir l'écart moyen : 

```bash
python src/pidr_calcul_diff_angle check -ref $(NOM_FICHIER_REFERENCE) -mes $(NOM_FICHIER_MESURE) -n $(SEUIL) 
```
NOM_FICHIER_REFERENCE : son chemin à partir du parcours relatif du fichier pidr, par exemple, Data/data_ref 

NOM_FICHIER_MESURE : son chemin à partir du parcours relatif du fichier pidr, par exemple, Data/data_web

SEUIL: Le niveau seuil pour valider ou invalider la justesse de la modélisation

_Exemple_

```bash
python src/pidr_calcul_diff_angle check -ref Data/data_ref.csv  -mes Data/data_mes.csv -n 0.5
```

### Help
Pour avoir plus d'informations concernant aux lignes de commandes, vous pouvez utiliser help :
```bash
python src/pidr_calcul_diff_angle --help
```
Pour avoir plus d'informations concernant aux lignes de commandes de chaque module, vous pouvez utiliser help :
```bash
python src/pidr_calcul_diff_angle $(COMMANDE) --help
```
Les modules accessibles sont check, courbe, decalage, scrapper, tout, pour voir plus de détails de chaque commande, il suffit de remplacer $(COMMANDE) par le nom de chaque module.

**Exemple**

Pour savoir plus d'informations du module scrapper, vous pouvez utiliser la ligne de commande suivante : 
```bash
python src/pidr_calcul_diff_angle scrapper --help
```
## Tests
Des tests unitaires sont également à votre disposition, pour exécuter les tests, il faut tout simplement exécuter la ligne de commande suivante :
```bash
pytest
```

## Pour plus d'informations 

 - [Module Selenium](https://selenium-python.readthedocs.io/installation.html)

 - [Site Web SunEarthTools ](https://www.sunearthtools.com/)

 - [Système de Coordonnées astronomiques](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_c%C3%A9lestes)

 - [Système de Coordonnées horizontales](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_horizontales)
