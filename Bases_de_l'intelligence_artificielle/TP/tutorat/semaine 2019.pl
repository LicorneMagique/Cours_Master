/* Question 1 

La modélisation utilisée pour représenter ce problème est un CSP. Il est demandé de trouver un résultat
à partir de postulat initiaux proche de enigme d'Einstein avec les maisons. Le but étant de trouver une 
réponse à partir de positions données à interpreter.
*/

/* Question 2 */

/*Se lit Y est le jour apres X*/
domaine([lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche]).

jour_apres(X,Y,[Y,_,_,_,_,_,X]).

jour_apres(X,Y,[X,Y|_]).

jour_apres(X,Y,[_,T2|Q]):-
    jour_apres(X,Y,[T2|Q]).

/*Se lit Y est le jour avant X*/
jour_avant(X,Y,L):-
    jour_apres(Y,X,L).

resoudre(S):-
    domaine(T),
    member(X,T),

    jour_apres(lundi,J1,T),
    X \== J1,

    jour_avant(jeudi,J2,T),
    X \== J2,

    jour_avant(dimanche,J3,T),
    X \== J3,

    jour_avant(J4,dimanche,T),
    X \== J4,

    jour_avant(samedi,J5TEMP,T),
    jour_avant(J5TEMP,J5,T),
    X \== J5,

    jour_apres(mercredi,J6TEMP,T),
    jour_apres(J6TEMP,J6,T),
    X \== J6,

    S = X.


/* Question 3 

Il n'y a qu'une seule réponse qui est dimanche, 

La requête pour afficher toutes les solutions est : 
findall(S, resoudre(S), L), write(L).
[dimanche]
L = [dimanche].
*/