# TP3

## Question 1.1

Hypothèses sur l'algorithme d’Itai-Rodeh :

- les nœuds n’ont plus forcément un identifiant unique,
- les nœuds connaissent le nombre total de nœuds `n`,
- chaque nœud connaît son voisin,
- communications FIFO.

## Question 1.2

Les nœuds doivent tous connaître `n` car avec des identifiants non uniques il est difficile de retrouver cette valeur ?  
Ou ils doivent tous connaître leur identifiant ?

## Question 1.3

Création d'un anneau unidirectionnel anonyme :

- on initialise `n` nœuds,
- on envoie à chaque nœud
  - son identifiant éventuellement non unique (random entre 0 et n-1 par exemple),
  - le `pid` de son voisin,
  - `n` le nombre de nœuds.

## Question 1.4

Donnez un exemple d’exécution de l’algorithme sur l’anneau à 4 nœuds :  
1 → 0 → 1 → 2 (le dernier nœud bouclant sur le 1er) avec k égal à 7 ([1; k] étant l’intervalle de tirage des identifiants pour chaque nœud).

```txt
1 → 0 → 1 → 2, n=4

Étape 1
1 devient actif, il passe en phase 1, il tire aléatoirement 3 dans [1,7], il envoie à 0 "id=1, phase=1, saut=1, unique=true"
0 devient actif, il passe en phase 1, il tire aléatoirement 2 dans [1,7], il envoie à 1 "id=0, phase=1, saut=1, unique=true"
1 devient actif, il passe en phase 1, il tire aléatoirement 6 dans [1,7], il envoie à 2 "id=1, phase=1, saut=1, unique=true"
2 devient actif, il passe en phase 1, il tire aléatoirement 3 dans [1,7], il envoie à 1 "id=2, phase=1, saut=1, unique=true"

Étape 2 :
flemme

```
