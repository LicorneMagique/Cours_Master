pair(0).
pair(X):-
    X > 0,
    X2 is X-2,
    pair(X2).


factoriel(0, 1).
factoriel(N, X):-
    N > 0,
    N1 is N-1,
    X1 is X/N,
    factoriel(N1, X1).

% u0 = 0,
fibo(0, 0).
% u1 = 1,
fibo(1, 1).
% uN = uN-1 + u N-2
fibo(N, X):-
    N > 1,
    N11 is N-1,
    N22 is N-2,
    fibo(N11, N1),
    fibo(N22, N2),
    X is N1 + N2.

affiche([]).
affiche([T|R]):-
    write(T),
    affiche(R).

afficheInv([]).
afficheInv([T|R]):-
    afficheInv(R),
    write(T).

premier([]).
premier([T|_]):-
    write(T).

premierBis([T|_], X):-
    X is T.

dernier([T|R]):-
    R == [], write(T).
dernier([_|R]):-
    R \= [], dernier(R).

dernierBis(L):-
    append(_,[X],L),
    write(X).

% la chèvre est un animal herbivore
animal(chevre).
herbivore(chevre).

% le loup est un animal cruel
animal(loup).
cruel(loup).

% un animal cruel est carnivore
carnivore(X) :-
    cruel(X).

% un animal carnivore mange de la viande
mange(X, viande) :-
    carnivore(X).

% un animal herbivore mange de l’herbe
mange(X, herbe) :-
    herbivore(X).

% un animal carnivore mange des animaux herbivores
mange(X, Y) :-
    carnivore(X),
    herbivore(Y).

% les carnivores et les herbivores boivent de l’eau
boit(X, eau) :-
    carnivore(X);
    herbivore(X).

% un animal consomme ce qu’il boit ou ce qu’il mange
consomme(X, Y) :-
    animal(X),
    (boit(X, Y);
    mange(X, Y)).

% Y-a-t-il un animal cruel et que consomme-t-il ?
test(X, Y) :-
    animal(X),
    cruel(X),
    consomme(X, Y).
