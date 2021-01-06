% Question 1 : Définir la base de faits contenant les maisons et les animaux, sans utiliser de listes
maison(pavillon).
maison(studio).
maison(chateau).

animal(chat).
animal(cheval).
animal(poisson).

% Question 2 : Traduire les trois premières phrases du casse-tête à l’aide du prédicat relation qui décrit la relation entre une personne, son animal et sa maison
% Marie a un chat
relation(marie, chat, M) :-
    maison(M).

% Rémy n’habite pas en pavillon.
relation(remy, A, M) :-
    animal(A),
    maison(M),
    M \== pavillon.

% Hugo habite un studio mais le cheval n'y est pas.
relation(hugo, A, studio) :-
    animal(A),
    A \== cheval.

% Question 3 : Définir le prédicat different(X,Y,Z) qui est vrai seulement si ses trois paramètres sont différents
different(X, Y, Z) :-
    X \= Y,
    Y \= Z,
    Z \= X.

% Chacun habite une maison différente et possède un animal distinct.
% La problématique à résoudre est : « Qui habite le château et qui a le poisson ? »

resoudre(A, B, C, D, E, F) :-
    relation(marie, D, A),
    relation(remy, E, B),
    relation(hugo, F, C),
    different(A, B, C),
    different(D, E, F).

personne(marie).
personne(remy).
personne(hugo).

relation2(A, B, C) :-
    personne(A),
    animal(B),
    maison(C).

resoudreRelations2([], [], []).
resoudreRelations2([TP|RP], [TA|RA], [TM|RM]) :-
    personne(TP),
    animal(TA),
    maison(TM),
    resoudreRelations2(RP, RA, RM).

different2([T|R], DT) :-
    T \= DT,
    different2(R, T).

different2([T|R]) :-
    different2(R, T).

resoudre2([P, A, M]) :-
    resoudreRelations2(P, A, M),
    different2(P),
    different2(A),
    different2(M).
