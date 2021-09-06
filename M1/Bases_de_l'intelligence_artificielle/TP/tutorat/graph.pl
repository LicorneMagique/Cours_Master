recherche(Ec,Ec,_,[]):-!.

recherche(Ec,Ef,Ltaboue,[Op|Lop]) :-
    operateur(Ec,Op,Es),
    not(interdit(Es)),
    not(member(Es,Ltaboue)),
    %write(Ec), write(' '), write(Op), write(' '),write(Es),nl,
    recherche(Es,Ef,[Es|Ltaboue],Lop).

resoudre(Sol) :- etatInitial(Ei),etatFinal(Ef),
    recherche(Ei,Ef,[Ei],Sol).


/* Fermier, loup, chèvre, chou */
etatInitial([g,g,g,g]).
etatFinal([d,d,d,d]).

/* Operateurs */
changerRive(g, d).
changerRive(d, g).
/* loup */
operateur([X,X,CHEVRE,CHOU], deplaceLoup ,[Y,Y,CHEVRE,CHOU]):-
    changerRive(X, Y).

/* chevre */
operateur([X,LOUP,X,CHOU], deplaceChevre ,[Y,LOUP,Y,CHOU]):-
    changerRive(X, Y).

/* chou */
operateur([X,LOUP,CHEVRE,X], deplaceChou ,[Y,LOUP,CHEVRE,Y]):-
    changerRive(X, Y).

/* fermier */
operateur([FERMIER,LOUP,CHEVRE,CHOU], deplaceSeul ,[FERMIER2,LOUP,CHEVRE,CHOU]):-
    changerRive(FERMIER, FERMIER2).

/* Interdits */

/* Loup x Chevre */
interdit([F,X,X,_]):-
    F \== X.

/* Chevre x Chou */
interdit([F,_,X,X]):- 
    F \== X.




/* Question 3 */
?- findall(Soluce ,resoudre(Soluce),L).
L = [
[deplaceChevre, deplaceSeul, deplaceLoup, deplaceChevre, deplaceChou, deplaceSeul, deplaceChevre], 
[deplaceChevre, deplaceSeul, deplaceChou, deplaceChevre, deplaceLoup, deplaceSeul, deplaceChevre]]




/* Exemple sujet 3 loups 3 chevres */
/*
[3,3,1,0,0,0]
[0,0,0,3,3,1]


interdit([X,Y,_,_,1]):- 
    X >= Y.

interdit([_,_,X,Y,1]):- 
    X >= Y.
*/
