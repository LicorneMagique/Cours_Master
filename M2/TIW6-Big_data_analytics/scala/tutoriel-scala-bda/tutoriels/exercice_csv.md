# Exercice: gestion de fichiers CSV & JSON

A titre d'exercice récapitulatif on se propose de faire un travail de préparation de données autour des information sur les VeloV à Lyon.

On dispose de deux fichiers (dans le répertoire `data`): 

* Le fichier [VeloV.sample.csv](../data/VeloV.sample.csv) contient des informations d'occupation sur les stations.
* Le fichier [stations.json](../data/stations.json) contient des informations sur les stations, en particulier leur position géographique.

## Travail sur le fichier CSV

Consulter la documentation de la bibliothèque [kantan.csv](https://index.scala-lang.org/nrinaudo/kantan.csv) qui permet de gérer les fichiers CSV.

Créer un programme Scala qui lit le fichier [VeloV.sample.csv](../data/VeloV.sample.csv) et créer un fichier CSV qui donne pour chaque station, chaque jour et chaque heure, le taux d'occupation moyen de la station. 

## Travail sur le fichier JSON

Consulter la documentation de la bibliothèque [spray-json](https://github.com/spray/spray-json) et celle de [Circe](https://circe.github.io/circe/) (+ [exercices](https://www.scala-exercises.org/circe/Json)) qui permettent de gérer les fichiers JSON. Choisir celle qui vous convient le mieux.

Modifier le programme précédent pour lire le fichier précédent afin de lire également le fichier [stations.json](../data/stations.json) de manière à filtrer la sortie en ne gardant que les stations situées dans le "rectangle" de coordonnées (lat: 45.733908 - 45.772373, long: 4.816069 - 4.838423).

## Détails techniques

Le schéma du fichier [VeloV.sample.csv](../data/VeloV.sample.csv) est le suivant:
```
(ID;timestamp;hour;day_of_week;available_bike_stands;available_bikes)
```

Exemple formaté d'élément du fichier [stations.json](../data/stations.json):
```json
{

    "number": 2010,
    "name": "02010 - CONFLUENCE DARSE",
    "address": "ANGLE ALEE ANDRE MURE ET QUAI ANTOINE RIBOUD",
    "position": {
        "lat": 45.743317,
        "lng": 4.815747
    },
    "banking": true,
    "bonus": false,
    "status": "OPEN",
    "contract_name": "Lyon",
    "bike_stands": 22,
    "available_bike_stands": 0,
    "available_bikes": 22,
    "last_update": 1483943073000

}
```