int getSommetMin(bool* presence, int* degre_courant, int n) {
    int sommet = -1;
    for (int i = 0; i < n; i++) {
        if (presence[i] && degre_courant[i] < degre_courant[sommet]) {
            sommet = i;
        }
    }
    return sommet;
}

void calcule_stable_max(bool* presence, int* degre_courant, graph* G, int sommet, // "x" le petit nom du sommet
                        bool* stable, int taille_stable, bool* stable_courant, int taille_stable_courant) {
    // Sauvegarde
    nodl* save;

    // mettre x dans le stable
    stable_courant[sommet] = true;
    taille_stable_courant++;

    // enlever x et ses voisins du graphe
    presence[sommet] = false; // mémorisé -> à inverser

    // enlever les voisins de x du graphe
    cell* voisin = G->links[sommet]->prem;
    while (voisin != NULL) {
        if (presence[voisin->node]) {
            inserer_en_queue(voisin->node, save); // mémorisé -> à inverser
            presence[voisin->node] = false; // on enlève le sommet
            cell* voisinVoisin = G->links[voisin->node]->prem;
            while (voisinVoisin != NULL) { // pour tous les voisins des voisins de x
                degre_courant[voisinVoisin->node]--; // on enlève 1 à leur degré
                voisinVoisin = voisinVoisin->suiv;
            }
        }
        voisin = voisin->suiv;
    }

    // Condition d'arrêt de la récursion
    // Sous quelle condition simple impliquant le nombre de sommets dans le
    // stable courant et le nombre de sommets dans le graphe induit courant peut on etre
    // sur que la branche en cours ne permettra pas de depasser la taille du stable maximum
    // trouve jusqu’a lors ?
    // if (taille_stable_courant < taille_stable) {
        // je ne suis pas sûr pour cette partie
    // }

    // Code algo récursif ici
    // pour tout sommet de degré min, calculer le stable max
    // selectionner un sommet y de degre courant minimum dans le nouveau graphe ainsi obtenu
    // faire les appels recursifs a calcule_stable_max pour chaque sommet parmi y et ses voisins
    int newSommet = getSommetMin(presence, degre_courant, G->n);
    if (newSommet != -1) { // si le graphe n'est pas vide
        calcule_stable_max(presence, degre_courant, G, newSommet, stable, taille_stable, stable_courant, taille_stable_courant);
        voisin = G->links[newSommet]->prem;
        while (voisin != NULL) {
            if (presence[voisin->node]) {
                calcule_stable_max(presence, degre_courant, G, voisin->node, stable, taille_stable, stable_courant, taille_stable_courant);
            }
        }
    } else { // si le graphe est vide
        // tester si le stable courant est mieux que le max enregistre, si oui mettre à jour
        if (taille_stable_courant > taille_stable) {
            taille_stable = taille_stable_courant;
            for (int i = 0; i < G->n; i++) {
                stable[i] = stable_courant[i];
            }
        }
    }

    // On remet tout dans l'état de départ
    voisin = save->prem;
    while (voisin != NULL) {
        presence[voisin->node] = true; // on remet le sommet
        cell* voisinVoisin = G->links[voisin->node]->prem;
        while (voisinVoisin != NULL) { // pour tous les voisins des voisins de x
            degre_courant[voisinVoisin->node]++; // on rajoute 1 à leur degré
            voisinVoisin = voisinVoisin->suiv;
        }
        voisin = voisin->suiv;
    }
    presence[sommet] = true; // on remet x à true
    stable_courant[sommet] = false; // on enlève x du stable
    taille_stable_courant--;
}
