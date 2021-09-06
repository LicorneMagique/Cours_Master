nombre(X) :-
    member(X, [1,2,3,4,5,6,7,8,9]).


differents([]).
differents([T|R]) :-
    not(member(T, R)),
    differents(R).

carre(S) :-
    nombre(A),
    nombre(B),
    differents([A,B]),
    nombre(C),
    differents([A,B,C]),
    L1 is A + B + C,
    nombre(D),
    differents([A,B,C,D]),
    nombre(E),
    differents([A,B,C,D,E]),
    nombre(F),
    differents([A,B,C,D,E,F]),
    L2 is D + E + F,
    L1 = L2,
    nombre(G),
    differents([A,B,C,D,E,F,G]),
    nombre(H),
    differents([A,B,C,D,E,F,G,H]),
    nombre(I),
    S = [A,B,C,D,E,F,G,H,I],
    differents(S),
    L3 is G + H + I,
    C1 is A + D + G,
    C2 is B + E + H,
    C3 is C + F + I,
    D1 is A + E + I,
    D2 is C + E + G,
    L1 = L3,
    L1 = C1,
    L1 = C2,
    L1 = C3,
    L1 = D1,
    L1 = D2.

% ?- carre(S).
% S = [2, 7, 6, 9, 5, 1, 4, 3, 8] ;
% S = [2, 9, 4, 7, 5, 3, 6, 1, 8] ;
% S = [4, 3, 8, 9, 5, 1, 2, 7, 6] ;
% S = [4, 9, 2, 3, 5, 7, 8, 1, 6] ;
% S = [6, 1, 8, 7, 5, 3, 2, 9, 4] ;
% S = [6, 7, 2, 1, 5, 9, 8, 3, 4] ;
% S = [8, 1, 6, 3, 5, 7, 4, 9, 2] ;
% S = [8, 3, 4, 1, 5, 9, 6, 7, 2] ;
% false.

% ?- findall(S, carre(S), R), length(R,L).
% R = [[2, 7, 6, 9, 5, 1, 4, 3|...], [2, 9, 4, 7, 5, 3, 6|...], [4, 3, 8, 9, 5, 1|...], [4, 9, 2, 3, 5|...], [6, 1, 8, 7|...], [6, 7, 2|...], [8, 1|...], [8|...]],
% L = 8.
