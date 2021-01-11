/*

    SEND
+   MORE
________
   MONEY

*/

different([]).
different([T|Q]) :-
    not(member(T, Q)),
    different(Q).

domaine([0,1,2,3,4,5,6,7,8,9]).

resoudre([S,E,N,D,M,O,R,Y]):-
    domaine(LIST),
    /*Init*/
    member(S, LIST),
    delete(LIST, S, LIST2),

    member(E, LIST2),
    delete(LIST2, E, LIST3),

    member(N, LIST3),
    delete(LIST3, N, LIST4),

    member(D, LIST4),
    delete(LIST4, D, LIST5),

    member(M, LIST5),
    delete(LIST5, M, LIST6),

    member(O, LIST6),
    delete(LIST6, O, LIST7),

    member(R, LIST7),
    delete(LIST7, S, LIST8),

    member(Y, LIST8),

    /* Contraintes */
    /* different([S,E,N,D,M,O,R,Y]), */

    S \== 0,
    M \== 0,
    
    
    SEND is S*1000 + E*100 + N*10 + D,
    MORE is M*1000 + O*100 + R*10 + E,
    MONEY is M*10000 + O*1000 + N*100 + E*10 + Y,

    SEND + MORE =:= MONEY.

/* 

    Alternative 1 :

    SEND is S*1000 + E*100 + N*10 + D,
    MORE is M*1000 + O*100 + R*10 + E,
    MONEY is M*10000 + O*1000 + N*100 + E*10 + Y,

    SEND + MORE =:= MONEY.

    Alternative 2 :

    D+E+(N+R)*10+(E+O)*100+(S+M)*1000 =:= Y + 10*E + 100*N + 1000*O + 10000*M

    Alternative 3 (to fix):

    D+E =:= Y mod 10,
    R1 is (D+E) // 10,

    N+R+R1 =:= E mod 10,
    R2 is (N+R+R1) // 10,

    E+O+R2 =:= N mod 10,
    R3 is (E+O+R2) // 10,

    S+M+R3 =:= O mod 10,
    R4 is (S+M+R3) // 10,

    M =:= R4.
*/


