# Compte-rendu de TP

## Consignes

Vous devrez rendre un compte-rendu de TP avant le 28 mai au soir

### Objectifs

Ce compte-rendu porte exclusivement sur les TP1 et TP2 et devra comprendre :

- un mini-rapport qui contiendra
  - les réponses aux questions des TP1 et TP2
  - des explications sur les programmes que vous avez réalisés.
    Ces explications doivent permettre à l’évaluateur de comprendre
    - comment vous êtes passé de l’algorithme au programme
    - quels sont les éléments que vous ajoutez à l’algorithme pour le rendre pratiquement fonctionnel ; 
- les programmes que vous avez réalisés.
  - Les exercices optionnels (exercice 3 pour le TP1 et exercice 4 pour le TP2) ne sont pas à traiter pour le rendu de TP et ne seront pas évalués.
  - Chaque programme (ou ensemble de programmes fonctionnant ensemble) devra être dans un fichier séparé afin que les évaluateurs puissent facilement les compiler et les exécuter ;

### Rendu

Ce compte-rendu sera soumis sous Tomuss dans la colonne ‘Rendu-TP’ (merci de ne pas soumettre une archive trop volumineuse)

### Notation

- 2 pts sur le travail réalisé en séance sur le TP1
- 2 pts sur le travail réalisé en séance sur le TP2
- 6 pts sur le compte-rendu
  - 2 pts sur la lisibilité des programmes
  - 2 pts sur la clarté des idées/réponses
  - 2 pts sur le fonctionnement des programmes)
- 10 pts attribuées lors des l’évaluation orale du 7 juin (les questions porteront sur votre rapport et vos programmes)

## TP1

### Question 1.1

- La foncion `main`
  - crée un thread qui exécutera la fonction `spawnedFunc`,
  - envoie à ce thread la valeur `196`,
  - affiche un message.
- Le `thread`
  - reçoit une valeur de type `int` dont la valeur est `196`,
  - affiche cette valeur dans un message.

Les fonctions importantes sont `send` et `receive`.

### Question 1.2

La communication mise en place entre ces deux processus est

- **bidirectionnelle**,
- **asynchrone** comme on peut s'y attendre avec un programme multithread,
- mais surtout les threads utilisent de l'**attente passive**.

### Question 2.1

- La fonction `main`
  - crée 10 threads dont elle mémorise les identifiants dans un tableau, ces threads exécuteront la fonction `spawnedFunc`,
  - envoie à chacun des threads fils l'identifiant de leur "thread fils suivant" pour mettre en place la topologie en anneau, en supposant que l'identifiant envoyé est le bon car le code qui récupère l'identifiant est à compléter *question 2*,
  - attend que tous les threads fils envoient un message pour indiquer qu'ils ont fini leur traitement.
- La fonction `spawnedFunc`
  - reçoit un objet de type Noeud,
  - extrait l'identifiant du thread de son "prochain voisin" à partir de cet objet,
  - envoie un message au thread parent pour indiquer qu'elle a terminé son traitement.

Les fonctions importantes sont toujours `send` et `receive` ainsi que `receiveAllFinalization` et `cast(T)` qui permet de transmettre tout type d'objet aux threads.

### Question 2.3

Soit `n` le nombre de threads de notre processus, l'anneau contient `n-1` threads car celui de la fonction `main` n'y est pas.

Après plusieurs tests je constate que `32 678` est le nombre maximum de threads qui peuvent fonctionner sur un processus de ma machine, ce résultat a été obtenu par dichotomie.

La taille maximale de l'anneau sur ma machine est donc `32 677`.

### Question 2.4

Chacun des `n` noeuds va exécuter `2` fois le contenu de la boucle for qui permet de compter les noeuds. Il y a donc `2n` messages échangés.

### Question 2.5 - Implémentation de l'horloge scalaire

L'initialisation se fait au lancement des threads avec le code suivant.

```d
int scalHorloge = 1;
```

L'incrémentation et la mise à jour de l'horloge se font avec le code suivant après chaque receive.

```d
// Le receive vient du noeud parent
scalHorloge++;

// Le receive vient d'un noeud voisin, le voisin nous a donc communiqué son horloge
scalHorloge = max(++scalHorloge, ++precScalHorloge);
```

L'envoi de l'horloge se fait à chaque fois que le noeud communique avec son voisin.

### Question 2.6 - Implémentation de l'horloge vectorielle

L'initialisation se fait au lancement des threads avec le code suivant.

```d
int[] vectHorloge = new int[n];
for (int i = 0; i < n; i++) {
    vectHorloge[i] = 0;
}
vectHorloge[myId] = 1;
```

L'incrémentation et la mise à jour de l'horloge se font avec le code suivant après chaque receive.

```d
// Le receive vient du noeud parent
vectHorloge[myId]++;

// Le receive vient d'un noeud voisin, le voisin nous a donc communiqué son horloge
for (int i = 0; i < precVectHorloge.length; i++) {
    if (precVectHorloge[i] > vectHorloge[i]) {
        vectHorloge[i] = precVectHorloge[i];
    }
}
vectHorloge[myId]++;
```

## TP2

### Question 1.1
