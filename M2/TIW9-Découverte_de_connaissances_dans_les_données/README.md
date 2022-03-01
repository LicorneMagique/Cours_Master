# Découverte de connaissances dans les données

## Notes

### Termes

- **Pattern mining** recherche de patterns dans les données (cause => conséquence)
- **Classification** séparation des données (symptomes : gens malades vs gens en bonne santé)
- **Clustering** regrouper des données similaires, faire des paquets de données
- **Regression** (**prédiction**) équivalent du pattern mining avec uniquement des valeurs numériques, prédiction des valeurs
- **Embeding** : représenter des données avec beaucoup de dimensions en des données avec moins de dimensions, à partir desquelles on peut regénérer des données similaires à l'entrée
- **Forme convexe** : forme qu'on peut facilement entourer avec des segments

### Clustering

C'est un problème :

- d'optimisation : minimisation de la similarité intra-cluster et maximisation de la similarité inter-cluster
- non supervisé : il n'est pas possible de vérifier rapidement et parfaitement si une solution est bonne

**Similarité** : elle est sensible au nombre de dimensions, il vaut mieux travailler sur des embedded pour limiter cet impact (beaucoup de 0 en commun)

### Normalisation

- **Min-max** : Le min devient 0, le max 1. Attention, risque que les données extrèmes écrasent les données moyennes
- **Z-score** : Distances avec les écart types

### Algo k-means

Cet algo passe à l'échelle avec une complexité presque linéaire car le nombre de cluster fixé par l'utilisateur est petit par rapport aux données. Attention il est sensible aux maximums locaux et il produit des clusters similaires en taille

### Algo EM, la généralisation de k-means

Cet algo fonctionne beaucoup mieux que k-means en utilisant des probabilités au lien des distances

### Hierarchical clustering

Fonctionne avec une matrice de similarité, on groupe les objets/clusters deux à deux jusqu'à n'avoir qu'un seul cluster parent

Relou si les données sont modifiées (il faut tout relancer), et complexité quadratique O(n²)

### Interactive pattern mining

> Apprendre en temps réel les préférence de l'utilisateur pour lui proposer des données qui correspondent à sa recherche (en gros)

#### Concept de l'anti-monotonie

Soit une combinaison de caractères type `[A-Z]+` dans un graphe avec la ralation de parent `parent(X, XY)`, `P(X)` ≥ `P(XY)`. Donc si on cherche `AQF`, inutile d'explorer les enfants de `B`…
