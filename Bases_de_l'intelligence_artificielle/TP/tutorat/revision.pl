compresse([],[]).

compresse([T],[T]).

compresse([T,T|Q],L1):-
    compresse([T|Q],L1).

compresse([T1,T2|Q],[T1|L1]):-
    compresse([T2|Q],L1).

/*
?- compresse([a,a,a,a,b,c,c,a,a,d,e,e,e,e],L1).
L1 = [a, b, c, a, d, e] .

?- compresse([],L).
L = [].
*/
appartient(_,[]):-
    false.
appartient(X,[X|_]):-
    true.
appartient(X,[T|Q]):-
    X =\= T,
    appartient(X,Q).

/*
?- appartient(2,[1,2,3,4,5]).
true .

?- appartient(2,[1,3,4,5]).
false.
*/
sous_ensemble([],_):-
    true.
sous_ensemble([T],L2):-
    appartient(T,L2).
sous_ensemble([T|Q],L2):-
    appartient(T,L2),
    sous_ensemble(Q,L2).
/*
?- sous_ensemble([1,3,5],[1,2,3,4,5,6,7,8,9]).
true .

?- sous_ensemble([1,3,5],[1,2,4,5,6,7,8,9]).
false.
*/

inverse([],[]).
inverse([T],[T]).
inverse([T|Q],LR):-
    inverse(Q,L),
    append([T],L,LR).
/*
?- inverse([1,2,3,4],L).
L = [1, 2, 3, 4] .
*/
sous_liste(_,[],_).
sous_liste(L1,[T1|Q1],[T2|Q2]):-
     T1 == T2 -> sous_liste(L1,Q1,Q2) ; sous_liste(L1,L1,Q2).
sous_liste([],_).
sous_liste(L1,L2):-
    sous_ensemble(L1,L2),
    sous_liste(L1,L1,L2).
/*
?- sous_liste([],[]).
true .

?- sous_liste([1],[]).
false.

?- sous_liste([4,5,6],[1,2,3,4,5,6,7,8,9]).
true .

?- sous_liste([4,5,6],[1,4,7,2,5,8,3,6,9]).
false.
*/

longueur([],0).
longueur([_|Q],N):-
    longueur(Q,Nt),
    N is Nt + 1.
/*
?- longueur([10,48,565,1231],N).
N = 4.

?- longueur([10],N).
N = 1.

?- longueur([],N).
N = 0.
*/

concat([],L2,L2).
concat([X|L1],L2,[X|L3]):-
    concat(L1,L2,L3).
/*
?- concat([1,2,3,4],[5,6,7,8,9],L).
L = [1, 2, 3, 4, 5, 6, 7, 8, 9].

?- concat([1,2,3,4],[],L).
L = [1, 2, 3, 4].

?- concat([561,989784651,84],[85456,845132,624845],L).
L = [561, 989784651, 84, 85456, 845132, 624845].

?- concat([],[],L).
L = [].
*/

palindrome(L):-
    reverse(L,L1),
    L1=L.
/*
?- palindrome([1,2,1]).
true.

?- palindrome([1,2,3]).
false.
*/
rang_pair([],[]).
rang_pair([_],[]).
rang_pair([_,T],[T]).
rang_pair([_,T|Q],Y):-
    rang_pair(Q,YR),
    append([T],YR,Y).
/*
?- rang_pair([a,b,c,d,e],L).
L = [b, d] .

?- rang_pair([],L).
L = [].
*/

indice(T,[T|_], 1).
indice(X,[_|Q],N):-
    indice(X,Q,Nt),
    N is Nt + 1.
/*
?- indice(5,[1,2,3,4,5,6,7,8,9],N).
N = 5 .

?- indice(5,[5,9,7,3,5],N).
N = 1 .

?- indice(5,[],N).
false.

?- indice(X,[589,1,1564,1,987],2).
X = 1 .
*/

remplace(_,_,[],[]).
remplace(X1,X2,[X1|Q],L2):-
    remplace(X1,X2,Q,LR),
    append([X2],LR,L2).
remplace(X1,X2,[T|Q],L2):-
    X1\=T,
    remplace(X1,X2,Q,LR),
    append([T],LR,L2).
/*
?- remplace(a,b,[a,a,t,t,v,v,va,a,a],L).
L = [b, b, t, t, v, v, va, b, b] .

?- remplace(a,b,[],L).
L = [] .
*/

partage([],_,[],[]).
partage([T|Q],X,L1,L2):-
    T < X,
    partage(Q,X,L1t,L2),
    append([T],L1t,L1).
partage([T|Q],X,L1,L2):-
    T >= X,
    partage(Q,X,L1,L2t),
    append([T],L2t,L2).
/*
?- partage([1,9,8,7,3,2,5,4,6],5,L1,L2).
L1 = [1, 3, 2, 4],
L2 = [9, 8, 7, 5, 6] .

?- partage([],5,L1,L2).
L1 = L2, L2 = [].
*/

somme([],_,0).
somme([T|Q],I,R):-
    somme(Q,I+1,Rs),
    R is Rs + T*I.
somme(L,R):-
    somme(L,1,R).

/*
?- somme([1,1,2,2,3,3],R).
R = 50.

?- somme([],R).
R = 0.

?- somme([4],R).
R = 4.
*/
