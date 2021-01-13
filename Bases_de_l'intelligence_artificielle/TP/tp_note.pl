% Julien Giraud 11704709


% Q1 il s'agit d'un problème de type CSP

% Q2
annee(X) :-
    member(X, [5, 20, 30, 40]).

cabine(X) :-
    member(X, [84, 164, 116, 248]).

personne(X) :-
    member(X, [gaetan, lucie, sophie, gabriel, karine, loic, andre, francoise]).

relation(H, F, A, C) :-
    personne(F),
    personne(H),
    annee(A),
    cabine(C).

relation(gaetan, lucie, A, 84) :-
    annee(A).

relation(M, sophie, 30, 164) :-
    personne(M).

relation(gabriel, F, 20, C) :-
    personne(F),
    F \== karine,
    cabine(C).

relation(loic, F, A, C) :-
    personne(F),
    annee(A),
    A \== 40,
    cabine(C).

relation(H, F, A, 116) :-
    personne(H),
    personne(F),
    relation(gaetan, lucie, Min, 84),
    annee(A),
    A > Min,
    A < 40.

differents([]).
differents([T|R]) :-
    not(member(T, R)),
    differents(R).

resoudre([A, B, C, D, E, F, G, H, I, J, K, L]) :-
    relation(gaetan, A, B, C),
    relation(gabriel, D, E, F),
    relation(loic, G, H, I),
    relation(andre, J, K, L),
    differents([A, D, G, J]),
    differents([B, E, H, K]),
    differents([C, F, I, L]).

% Q3
% findall(S, resoudre(S), T), length(T, L).
% J'ai clairement un problème de boucle infinie dans ma modélisation, je ne peux donc pas conclure
