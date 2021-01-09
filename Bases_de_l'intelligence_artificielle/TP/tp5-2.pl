% Problème
initial([0,0]).
final([4,_]).
final([_,4]).

remplir5().
remplir8().
transvaser(transvaser5vers8).
transvaser(transvaser8vers5).
vider(vider5).
vider(vider8).

operateur([Grande,Petite], transvaser8vers5, [NouvelleGrande,NouvellePetite]) :-
    ResteLibreDans5 is (5-Petite),
    NouvelleGrandeTemp is (Grande - ResteLibreDans5),
    NouvelleGrande is max(NouvelleGrandeTemp, 0),
    NouvellePetite is (Petite + Grande - NouvelleGrande).

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
