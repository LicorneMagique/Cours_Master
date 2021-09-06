nombre(X) :-
    member(X, [1,2,3,4,5,6,7,8,9]).

somme(A, B, C) :-
    X is A + B + C,
    X = 15.

unique([T|R]) :-
    not(member(T, R)),
    unique(R).

carre([A, B, C, D, E, F, G, H, I]) :-
    nombre(A),
    nombre(B),
    nombre(C),
    nombre(D),
    nombre(E),
    nombre(F),
    nombre(G),
    nombre(H),
    nombre(I),
    unique([A,B,C,D,E,F,G,H,I]),
    somme(A, B, C),
    somme(D, E, F),
    somme(G, H, I),
    somme(A, D, G),
    somme(B, E, H),
    somme(C, F, I),
    somme(A, E, I),
    somme(C, E, G).
