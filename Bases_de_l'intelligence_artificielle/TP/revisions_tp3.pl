animal(chat).% Marie a un chat.
animal(cheval).
animal(poisson).

maison(pavillon).
maison(studio).
maison(chateau).

relation(marie, chat, X) :-
    maison(X).

% Rémy n’habite pas en pavillon.
relation(remy, X, Y) :-
    animal(X),
    maison(Y),
    Y \== pavillon.

% Hugo habite un studio mais le cheval n'y est pas.
relation(hugo, X, studio) :-
    animal(X),
    X \== cheval.

different(X, Y, Z) :-
    X \== Y,
    X \== Z,
    Y \== Z.
% Chacun habite une maison différente et possède un animal distinct.

% La problématique à résoudre est : « Qui habite le château et qui a le poisson ? »

probleme(A, B, C, D, E, F) :-
    relation(marie, A, D),
    relation(remy, B, E),
    relation(hugo, C, F),
    different(A, B, C),
    different(D, E, F).
