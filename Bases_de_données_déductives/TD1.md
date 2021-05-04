# TD 1 : Introduction à la Logique du Premier Ordre et Datalog

∃ ≡ ∀ ⇒

## Exercice 1. (Modélisation)

Préciser à l’aide d’un quantificateur le sens de “un” dans les phrases suivantes et formaliser les en logique des prédicats :

1. Jean suit un cours.

    Prédicats : cours^1, Jean^0, suivre^2

    ∃c cours(c) && suivre(Jean, c)

2. Un logicien a été champion du monde de cyclisme.

    Prédicats : logicien^1, champion^1

    ∃h logicien(h) && champion(h)

3. Un entier naturel est pair ou impair.

    Prédicats : entier^1, pair^1, impaire^1

    ∀n entier(n) && (pair(n) && !impaire(n) || !pair(n) && impaire(n))

4. Un enseignant-chercheur a toujours un nouveau sujet à étudier.

    Prédicats : enseignantChercheur^1, nouveauSujet^1, étudier^2

    ∀e,∃s enseignantChercheur(e) && nouveauSujet(s) && étudier(e, s)

5. Dans un triangle isocèle il existe une médiane qui est également hauteur.

    ∀x triangle(x) && iso(x) -> ∃y mediane(m, x) && hauteur(m, x)

6. Dans un triangle équilatéral toute médiane est également hauteur.

    Prédicats : triangleEqui^1, mediane^2, hauteur^2

    ∀t triangleEqui(t) -> ∀m mediane(m, t) && hauteur(m, t)

## Exercice 2. (Modélisation 2)

Formaliser les phrases suivantes en logique des prédicats :

1. Un cheval est plus rapide qu’un chien.
2. Il existe un lévrier qui est plus rapide que tout lapin.
3. Tout lévrier est un chien.

    Prédicats : chien^1 , levrier^1

    ∀x levrier(x) -> chien(x)

4. Harry est un cheval.

    Prédicats : cheval^1, Harry^0

    cheval(Harry)

5. Ralph est un lapin.

    Prédicats : lapin^1; , Ralph^0

    lapin(Ralph)

6. La relation être plus rapide que est transitive.

## Exercice 3. (Modélisation 3)

Représenter la phrase “Tout nombre entier naturel x a un successeur qui est inférieur ou égal à tout entier strictement supérieur à x” par une formule logique en utilisant les prédicats suivants :

- entier(x)
- successeur(x, y)
- inf (x, y)
- “est un entier naturel”
- “est successeur de y”
- “est inférieur ou égal à y”

## Exercice 4. (SQL et Datalog)

Considérez la relation Flight :  
Flights(fino : integer, from : string, to : string, distance : integer, departs : time, arrives : time)

Question : Donnez la requête en Datalog et SQL pour les phrases suivantes :

1. Trouvez le fino de tous les vols au départ de Madison.
2. Trouvez le fino de tous les vols qui quittent Chicago après que le vol 101 arrive à Chicago au plus tard une heure après.
3. Trouvez le fino de tous les vols qui ne partent pas de Madison.
4. Trouver toutes les villes accessibles de Madison à travers une série d’un ou plusieurs vols de correspondance.
5. Trouver toutes les villes accessibles à partir de Madison à travers une chaîne d’un ou plusieurs vols de correspondance, avec pas plus d’une heure passée sur n’importe quelle correspondance. (C’est-à-dire, chaque vol de correspondance doit partir au plus tard une heure après l’arrivée du vol précédent dans la chaîne.)
6. Trouver le fino de tous les vols qui ne partent pas de Madison ou une ville qui est accessible de Madison à travers une chaîne de vols.
