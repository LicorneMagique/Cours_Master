animal(loup).
animal(chevre).

herbivore(chevre).
cruel(loup).


% • un animal cruel est carnivore
cruel(X):-
    carnivore(X).

% • un animal herbivore mange de l’herbe
mange(X, Y):-
    herbivore(X),
    Y = herbe.

% • un animal carnivore mange des animaux herbivores
mange(X, Y):-
    carnivore(X),
    herbivore(Y).

% • un animal carnivore mange de la viande
carnivore(X):-
    mange(X, viande).


% • les carnivores et les herbivores boivent de l’eau
boire(X, eau):-
    carnivore(X).
boire(X, eau):-
    herbivore(X).

% un animal consomme ce qu’il boit ou ce qu’il mange
consomme(X, Y):-
    boire(X, Y).
consomme(X, Y):-
    mange(X, Y).

% Y-a-t-il un animal cruel et que consomme-t-il ?
% Vous devez obtenir que le loup est cruel et qu’il mange de la viande, des chèvres et de l’eau.
