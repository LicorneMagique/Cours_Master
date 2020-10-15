# TP1

À rendre le 18 décembre

## Lancement

```shell
make clean; make; valgrind --leak-check=full --show-leak-kinds=all ./mincut -i data/graphEL_as2000 -o output
```

## Questions

1. Compilez le programme. Combien d’options a-t-il ? À quoi servent-elles ? Quelles sont les valeurs par défaut ?

    ```shell
    Usage: ./mincut -h
      -h: print current help.
      -i "inputname": input file containing the graph (default value is stdin).
      -o "outputname": output results in a file named "outputname" (default value is stdout).

    ```

2. À quoi sert la fonction `graph_from_file` du fichier auxiliaire.c ? Quelle autre fonction de manipulation de graphe ce fichier contient-il ?

    Construit un graphe à partir d'un fichier et renvoie un pointeur sur la structure.  
    Il y a la fonction `write_graph` qui fait exactement l'inverse.

3. Comment est representé un graphe ? De quel type de graphe s’agit-il ?

    ```c
    typedef struct graph{
      int n; // compte le nombre de noeud du graphe
      int m; // compte le nombre d'arêtes
      nodl** links; // tableau contenant les arêtes
      int *degrees; // tableau qui associe à chaque noeud son degré
    } graph;
    ```

4. Quelle structure stocke une liste d’adjacence ? De quel type de liste s’agit-il ?

    - Ensemble de listes non ordonnées
    - Chaque liste décrit l'ensemble des voisins d'un sommet dans le graphe, autrement dit ça représente un graphe

5. Dans le fichier auxiliaire.c, écrivez une fonction free_nodl qui libère entièrement l’espace mémoire occupé par une liste de noeuds, donnée par un pointeur vers la liste. Attention, il faut libérer l’espace occupé par chacune des cellules de la liste !  
De même, écrivez une fonction free_graph qui libère entièrement l’espace mémoire occupé par un graphe, là encore donné par un pointeur sur le graphe.

    Indication. Avant de vous lancer, lisez l’annexe A sur la gestion de la mémoire en C. Pour l’instant, le programme se contente d’ouvrir les fichiers d’entrée et de sortie specifiés lors de l’appel au programme, respectivement en lecture seule et écriture seule, et de les fermer à la fin du programme.

6. Complétez le main pour que le programme :

    - charge un graphe G en mémoire à partir du fichier spécifié en entrée (ou de l’entrée standard),
    - écrive sur la sortie d’erreur standard (stderr) le nombre de sommets et le nombre d’arêtes du graphe chargé,
    - écrive le graphe chargé dans le fichier spécifié en sortie (ou sur la sortie standard) et
    - libère la place prise par le graphe en memoire avant de quitter.

    Vous fermerez le fichier d’entrée immédiatement après avoir chargé le graphe qu’il contient, à l’aide de la fonction fclose, déjà utilisée à la fin du main.

    Indication. Vous trouverez de nombreux exemples d’écriture dans un fichier ou sur les sorties standard dans les fichiers main.c et auxiliaire.c qui vous sont fournis. L’annexe B du sujet contient également un petit rappel sur l’utilisation de la fonction fprintf.

    Plusieurs fichiers qui contiennent chacun un graphe, et dont le nom est de la forme graphEL_*, vous sont donnés dans le dossier /data accessible depuis la page web des TP (voir descriptif succint de leur provenance dans la section 3).  
    Le format qu’ils utilisent pour encoder le graphe G est le suivant :

    - la première ligne du fichier contient le nombre n de sommets dans le graphe,
    - toutes les autres lignes du fichier contiennent une arête du graphe sous la forme de deux entiers u v séparés par un espace, ou u et v sont les identifiants des deux sommets (distincts) qui sont les extremités de l’arête,
    - l’identifiant d’un sommet est un entier compris entre 0 et n - 1.

7. Essayez votre programme sur quelques-uns des graphes fournis, en par-
ticulier sur toygraph et toygraph2. Y a-t-il des différences entre le fichier d’entrée et le fichier de sortie écrit par la fonction write_graph ? D’où viennent ces différences ?

    Indication. Si besoin (pour les gros fichiers), vous pouvez comparez le contenu des deux fichiers de manière automatique grâce à la commande diff fic1 fic2 du système d’exploitaion.

8. Avant de continuer, dans le main, gardez la partie du code qui charge le
graphe en mémoire et retirez celle qui l’écrit dans le fichier de sortie (dans la suite, on va s’occuper d’y écrire le résultat de l’algorithme).
