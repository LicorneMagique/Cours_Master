/* les hommes */
homme(alphonse).
homme(bernard).
homme(cedric).
homme(david).
homme(fabien).
homme(gerard).
homme(hubert).
homme(jules).
homme(kevin).
homme(lucien).

/* les femmes */
femme(charlotte).
femme(daniela).
femme(eloise).
femme(marie).
femme(nathalie).
femme(ophelie).
femme(stephanie).
femme(violette).
femme(zoe).

/* les relations de parenté */
/* où enfant(X,Y) signifie que X est enfant de Y */
enfant(alphonse,bernard).
enfant(alphonse,eloise).
enfant(cedric,fabien).
enfant(cedric,nathalie).
enfant(daniela,kevin).
enfant(daniela,charlotte).
enfant(fabien,lucien).
enfant(fabien,marie).
enfant(gerard,lucien).
enfant(gerard,marie).
enfant(nathalie,david).
enfant(nathalie,zoe).
enfant(ophelie,hubert).
enfant(ophelie,marie).
enfant(stephanie,alphonse).
enfant(stephanie,violette).
enfant(violette,zoe).
enfant(violette,jules).
enfant(charlotte,zoe).
enfant(charlotte,jules).

parent(X,Y):-
    enfant(Y,X).

mere(X,Y):-
    enfant(Y,X),
    femme(X).

pere(X,Y):-
    parent(Y,X),
    homme(Y).

grand_parent(X,Y):- % X est le parent du parent de Y
    parent(Z, Y),
    parent(X, Z).

grand_mere(X,Y):-
    grand_parent(X,Y),
    femme(X).

grand_pere(X,Y):-
    grand_parent(X,Y),
    homme(X).

ancetre(X,Y):-
    parent(X,Y).

ancetre(X,Y):-
    parent(X,Z),
    ancetre(Z,Y).

% Q1
% Est-ce que Cedric est un homme ?
% homme(cedric).
% Cedric est-il un enfant de Charlotte ?
% enfant(cedric, nathalie).