rechPf(Ef, Ef, _, []).
rechPf(Ec, Ef, L1, L2) :-
    operateur(Ec, Opx, Es),
    not(member(Es, L1)),
    not(interdit(Es)),
    rechPf(Es, Ef, [Ec|L1], Y),
    L2 = [Opx|Y].

:- dynamic interdit/1.

resoudre(S) :-
    initial(Ei),
    final(Ef),
    rechPf(Ei, Ef, [], S).

initial([0,0]).
final([4,_]).
final([_,4]).

operateur([Petite, Grande], remplirPetite, [5, Grande]) :-
    Petite < 5.

operateur([Petite, Grande], remplirGrande, [Petite, 8]) :-
    Grande < 8.

operateur([Petite, Grande], viderPetite, [0, Grande]) :-
    Petite > 0.

operateur([Petite, Grande], viderGrande, [Petite, 0]) :-
    Grande > 0.

operateur([Petite, Grande], transvaserPetiteDansGrande, [NewPetite, NewGrande]) :-
    Qmax is 8 - Grande,
    (
        Petite =< Qmax, Q is Petite;
        Petite > Qmax, Q is Qmax
    ),
    Qmax > 0,
    Q > 0,
    NewPetite is Petite - Q,
    NewGrande is Grande + Q.


operateur([Petite, Grande], transvaserGrandeDansPetite, [NewPetite, NewGrande]) :-
    Qmax is 5 - Petite,
    (
        Grande =< Qmax, Q is Grande;
        Grande > Qmax, Q is Qmax
    ),
    Qmax > 0,
    Q > 0,
    NewPetite is Petite + Q,
    NewGrande is Grande - Q.

% ?- resoudre(S).
% S = [remplirPetite, remplirGrande, viderPetite, transvaserGrandeDansPetite, viderPetite, transvaserGrandeDansPetite, remplirGrande, transvaserGrandeDansPetite, viderPetite|...] ;
% S = [remplirPetite, remplirGrande, viderPetite, transvaserGrandeDansPetite, viderPetite, transvaserGrandeDansPetite, remplirGrande, transvaserGrandeDansPetite, viderPetite|...]

% ?- findall(S, (resoudre(S)), T), length(T, L).
% T = [[remplirPetite, remplirGrande, viderPetite, transvaserGrandeDansPetite, viderPetite, transvaserGrandeDansPetite, remplirGrande, transvaserGrandeDansPetite|...], [remplirPetite, remplirGrande, viderPetite, transvaserGrandeDansPetite, viderPetite, transvaserGrandeDansPetite, remplirGrande|...], [remplirPetite, transvaserPetiteDansGrande, remplirPetite, remplirGrande, viderPetite, transvaserGrandeDansPetite|...], [remplirPetite, transvaserPetiteDansGrande, remplirPetite, remplirGrande, viderPetite|...], [remplirPetite, transvaserPetiteDansGrande, remplirPetite, transvaserPetiteDansGrande|...], [remplirPetite, transvaserPetiteDansGrande, remplirPetite|...], [remplirPetite, transvaserPetiteDansGrande|...], [remplirPetite|...], [...|...]|...],
% L = 102.

% ?- findall(S, (resoudre(S), length(S, 10)), T), length(T, L), write(T).
% [[remplirPetite,transvaserPetiteDansGrande,remplirPetite,transvaserPetiteDansGrande,viderGrande,transvaserPetiteDansGrande,remplirPetite,transvaserPetiteDansGrande,remplirPetite,transvaserPetiteDansGrande]]
% T = [[remplirPetite, transvaserPetiteDansGrande, remplirPetite, transvaserPetiteDansGrande, viderGrande, transvaserPetiteDansGrande, remplirPetite, transvaserPetiteDansGrande|...]],
% L = 1.
