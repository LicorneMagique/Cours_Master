/* Exemple de modélisation avec liste (non terminée) */

domaine([marie, alexis, remi, nathalie, olivier]).

placement([RC,E1,E2,E3,E4]):-
    domaine(X),
    member(RC, X),
    member(E1, X),
    E1 \== RC,
    member(E2, X),
    E2 \== RC, E2 \== E1,
    member(E3, X),
    E3 \== RC, E3 \== E1, E3 \== E2,
    member(E4, X),
    E4 \== RC, E4 \== E1, E4 \== E2, E4 \== E3.

/* Se lit X a cote de Y dans L*/
acote(X,Y,L):-
    TODO.
    
contrainte1([_,_,_,_,E4]):-
    E4 \== marie.

contrainte2([RC,_,_,_,E4]):-
    RC \== remi,
    E4 \== remi.

contraine3(L).

contrainte4(L).

resoudre(L):-
    /* Init */
    placement(L),

    /* Contraintes */
    contrainte1(L),
    contrainte2(L),
    contrainte3(L),
    contrainte4(L).


