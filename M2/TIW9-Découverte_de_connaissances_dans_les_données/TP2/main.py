"""
TIW9: Clustering de time-series

Jeremy Thomas (11702137)
Julien Giraud (11704709)

Pour modifier le jeu de données, modifier la variable file_name dans la fonction main.
"""

import time
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hac
import pandas as pandas
from tslearn.clustering import TimeSeriesKMeans
from tslearn.metrics import dtw as dtw_score
from dtaidistance import ed, dtw
from scipy.cluster.hierarchy import ClusterWarning
from warnings import simplefilter
simplefilter("ignore", ClusterWarning)


# Extraire les données time series du jeu de données et les regroupe par classe
def get_time_series_by_class_from_file(file_path):
    time_series_by_class = {}
    with open(file_path, 'r') as file_path:
        for row in file_path.readlines():
            row = row.split(',')
            class_serie = int(row[0])
            time_serie = [float(x) for x in row[1:]]
            if class_serie not in time_series_by_class:
                time_series_by_class[class_serie] = [time_serie]
                continue
            time_series_by_class[class_serie].append(time_serie)
    return time_series_by_class


# Extraire les données time series dans une matrice, supprimant les classes
def extract_time_series_without_class(data):
    time_series = []
    for class_serie in data:
        for time_serie in data[class_serie]:
            time_series.append(time_serie)
    return time_series


def hierarchical_clustering(data, distance_method, file_name):
    data = extract_time_series_without_class(data)
    if distance_method.lower() == "dtw":
        distances = dtw.distance_matrix(data)
    else:
        distances = []
        for x in range(len(data)):
            distance = []
            for y in range(len(data)):
                distance.append(ed.distance(data[x], data[y]))
            distances.append(distance)
    data = pandas.DataFrame(data=distances)

    model = hac.linkage(data)
    plt.figure(figsize=(20, 10))
    plt.xlabel('Time Serie')
    plt.ylabel('Distance')
    plt.title(
        "{} Hierarchical Clustering ({})".format(file_name, distance_method),
        fontsize=25,
        loc='left',
        color="red"
    )
    plt.draw()
    hac.dendrogram(
        model,
        leaf_rotation=90.,
        leaf_font_size=8.,
    )
    plt.show()


def kmeans_clustering(data, distance_method, file_name):
    model = TimeSeriesKMeans(
        n_clusters=len(data),
        metric=distance_method.lower(),
    )

    time_series = extract_time_series_without_class(data)
    axis_x = [x for x in range(len(time_series[0]))]
    model.fit(time_series)
    fig, graph = plt.subplots()
    fig.set_figwidth(20)
    fig.set_figheight(10)
    graph.set_xlabel('Time Serie')
    graph.set_ylabel('Unit')
    plt.title(
        "{} K-means Clustering ({})".format(file_name, distance_method),
        fontsize=25,
        loc='left',
        color="red"
    )
    sum_score = 0
    compteur = 0
    for time_serie in time_series:
        compteur += 1
        plt.plot(axis_x, time_serie, lw=1)
        plt.draw()
        score = dtw_score(time_serie, model.cluster_centers_[0])
        for class_serie in range(1, len(data)):
            temp_score = dtw_score(time_serie, model.cluster_centers_[class_serie])
            if temp_score < score:
                score = temp_score
        sum_score += score

    # Calcul de la moyenne du score : somme_score/nombre_serie
    avg = sum_score / len(time_series)
    for class_serie in range(len(data)):
        plt.plot(axis_x, model.cluster_centers_[class_serie], c="red", lw=8)
        plt.draw()
    plt.show()
    return avg


# Récupère le chemin du fichier correspondant au nom indiqué dans la varialble file_name.
# Le nom doit correspondre à un dossier présent dans le dossier data
def get_path_of_file(file_name):
    return 'data/' + file_name + "/" + file_name + "_TRAIN"


# Démarre le clustering (hiérarchique et k-means) avec pour chacun le calcul des distances euclidiennes et DTW
def main():
    # Nom du dossier contenant le jeu de données
    file_names = ["ECGFiveDays", "Gun_Point"]

    for file_name in file_names:
        # K-means Clustering DTW and EUCLIDEAN
        print("K-means Clustering with DTW...")
        start_kmeans_dtw = time.time()
        kmeans_similarity_dtw = kmeans_clustering(get_time_series_by_class_from_file(get_path_of_file(file_name)), 'DTW', file_name)
        end_kmeans_dtw = time.time()
        print("K-means Clustering with EUCLIDEAN...")
        start_kmeans_euclidean = time.time()
        kmeans_similarity_euclidean = kmeans_clustering(get_time_series_by_class_from_file(get_path_of_file(file_name)), 'EUCLIDEAN', file_name)
        end_kmeans_euclidean = time.time()
        # Hierarchical Clustering DTW and EUCLIDEAN
        print("Hierarchical Clustering with DTW...")
        start_hierarchical_dtw = time.time()
        hierarchical_clustering(get_time_series_by_class_from_file(get_path_of_file(file_name)), 'DTW', file_name)
        end_hierarchical_dtw = time.time()
        print("Hierarchical Clustering with EUCLIDEAN...")
        start_hierarchical_euclidean = time.time()
        hierarchical_clustering(get_time_series_by_class_from_file(get_path_of_file(file_name)), 'EUCLIDEAN', file_name)
        end_hierarchical_euclidean = time.time()

        print("Score moyen entre les time-series et le cluster généré (DTW): {} (Lower is better)"
            .format(round(kmeans_similarity_dtw, 2)))
        print("Score moyen entre les time-series et le cluster généré (distance Euclidiennes): {} (Lower is better)"
            .format(round(kmeans_similarity_euclidean, 2)))
        print("Temps d'exécution du clustering K-means avec DTW : {} seconde(s)"
            .format(round((end_kmeans_dtw - start_kmeans_dtw), 2)))
        print("Temps d'exécution du clustering K-means avec distances Euclidiennes : {} seconde(s)"
            .format(round((end_kmeans_euclidean - start_kmeans_euclidean), 2)))
        print("Temps d'exécution du clustering hiérarchique avec DTW : {} seconde(s)"
            .format(round((end_hierarchical_dtw - start_hierarchical_dtw), 2)))
        print("Temps d'exécution du clustering hiérarchique avec distances Euclidiennes : {} seconde(s)"
            .format(round((end_hierarchical_euclidean - start_hierarchical_euclidean), 2)))


try:
    main()
except Exception as e:
    print(e)
