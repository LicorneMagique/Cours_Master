initial([g,g,g,g,g]).
final([d,d,d,d,d]).

inverse(d,g).
inverse(g,d).

% en premier ya la barque
operateur([X, X, Mere, E1, E2], pere, [NX, NX, Mere, E1, E2]) :-
    inverse(X, NX).
operateur([X, Pere, X, E1, E2], mere, [NX, Pere, NX, E1, E2]) :-
    inverse(X, NX).
operateur([X, Pere, Mere, X, E2], e1, [NX, Pere, Mere, NX, E2]) :-
    inverse(X, NX).
operateur([X, Pere, Mere, E1, X], e2, [NX, Pere, Mere, E1, NX]) :-
    inverse(X, NX).
operateur([X, Pere, Mere, X, X], e1e2, [NX, Pere, Mere, NX, NX]) :-
    inverse(X, NX).

:- dynamic interdit/1.

rechPf(Ef, Ef, _, []).
rechPf(Ec, Ef, L1, L2) :-
    operateur(Ec, Opx, Es),
    not(member(Es, L1)),
    not(interdit(Es)),
    rechPf(Es, Ef, [Ec|L1], Y),
    L2 = [Opx|Y].

resoudre(S) :-
    initial(Ei),
    final(Ef),
    rechPf(Ei, Ef, [], S).

salaireSansPrime(X) :-
    member(A, [1,2,3,4,5,6,7,8,9]),
    member(B, [0,1,2,3,4,5,6,7,8,9]),
    member(C, [0,1,2,3,4,5,6,7,8,9]),
    member(D, [0,1,2,3,4,5,6,7,8,9]),
    C is A + B,
    C2 is A * B,
    C == C2,
    D is 0,
    X is 1000 * A + 100 * B + 10 * C + D.

salaire(Salaire) :-
    salaireSansPrime(X),
    Salaire is (X + X / 10).
