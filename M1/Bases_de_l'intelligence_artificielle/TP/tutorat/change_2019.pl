selection(X):-
    member(X, [0,1,2,3,4,5,6,7,8,9]).

resoudre(Somme, [B1,B2,B5,B20]):-
 
    /* Select nombre billet */
    selection(B1),
    selection(B2),
    selection(B5),
    selection(B20),

    /* Check Condition */
    B1+B2+B5+B20 =:= 10,
    B1*1+B2*2+B5*5+B20*20 =:= Somme.

/*
findall(S, resoudre(61), L), write(L).
*/