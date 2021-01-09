% Ei état initial
% initial(Ei).

% Ef état final
% final(Ef).

% Ec état courant
% Opx opérateur de transition
% Es état de sortie, atteint par application de Opx
% operateur(Ec,Opx,Es).

% Problème
initial(entree).
final(sortie).
interdit(minotaure).
couloir(entree, thesee).
couloir(entree, ariane).
couloir(thesee, minotaure).
couloir(thesee,sombre).
couloir(claire, sombre).
couloir(claire, sortie).
couloir(minotaure, sortie).
couloir(ariane, claire).
couloir(sombre,sortie).
operateur(E1,[E1,E2],E2) :-
    couloir(E1,E2).
operateur(E1,[E1,E2],E2) :-
    couloir(E2,E1).

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
