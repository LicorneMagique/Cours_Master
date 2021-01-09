% regle(Ri, ListeDePrémisses, ListeDeConclusions).
regle(r1, [a, b], [c]).
regle(r2, [c, non(d)], [f]).
regle(r3, [f, b], [e]).
regle(r4, [f, a], [non(g)]).
regle(r5, [non(g)], [b]).
regle(r6, [a, h], [l]).

faits([]).
faits([non(T)|R]) :-
    assert(faux(T)),
    faits(R).
faits([T|R]) :-
    assert(vrai(T)),
    faits(R).

raz() :-
    retractall(vrai(_)),
    retractall(faux(_)).

:- dynamic vrai/1, faux/1.

premissesOk([]).
premissesOk([T|R]) :-
    vrai(T),
    premissesOk(R).

saturer(Regles) :-
    regle(R, Premisses, Conclusions), % je prends une règle
    premissesOk(Premisses), % si ses conditions sont validées
    not(member(R, Regles)),
    append(Regles, [R], NewRegles), % je l'utilise
    faits(Conclusions), % j'ajoute ses conclusions
    saturer(NewRegles).
