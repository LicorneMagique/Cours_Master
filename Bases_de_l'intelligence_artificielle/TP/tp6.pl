% regle(Ri, ListeDePrémisses, ListeDeConclusions).
regle(r1, [a, b], [c]).
regle(r2, [c, non(d)], [f]).
regle(r3, [f, b], [e]).
regle(r4, [f, a], [non(g)]).
regle(r5, [non(g)], [b]).
regle(r6, [a, h], [l]).

faits([]).
faits([non(T)|R]) :-
    assert(faux(T)),
    faits(R).
faits([T|R]) :-
    assert(vrai(T)),
    faits(R).

raz() :-
    retractall(vrai(_)),
    retractall(faux(_)).

:- dynamic vrai/1, faux/1, utilise/1.

premissesOk([]).
premissesOk([T|R]) :-
    vrai(T),
    premissesOk(R).

vrai(non(X)) :-
    faux(X).

doSaturer2(ReglesUtilisees, ReglesEssayees) :-
    regle(R, Premisses, Conclusions), % je prends une règle
    not(member(R, ReglesEssayees)),
    append([R], ReglesEssayees, NewReglesEssayees),

    not(member(R, ReglesUtilisees)), % si elle n'a pas déjà été utilisée,
    premissesOk(Premisses), % et que ses conditions sont validées
    append([R], ReglesUtilisees, NewReglesUtilisees),
    write(Conclusions),
    faits(Conclusions), % j'ajoute ses conclusions
    write("J'utilise " + R + "\n"),
    write(R + " prouve " + Conclusions),

    doSaturer(NewReglesUtilisees, NewReglesEssayees);

    doSaturer(ReglesUtilisees, NewReglesEssayees).

print([]) :-
    write("\n").
print([T|R]) :-
    write(T),
    write(" "),
    print(R).

doSaturer(ReglesUtilisees, ReglesEssayees) :-
    regle(R, Premisses, Conclusions), % je prends une règle
    not(member(R, ReglesEssayees)),
    % write("J'essaie "),
    % write(R),
    % write("\n"),
    append([R], ReglesEssayees, NewReglesEssayees),
    (
        not(member(R, ReglesUtilisees)),
        % print(R, "n'est pas utilisé"),
        premissesOk(Premisses), % et que ses conditions sont validées
        append([R], ReglesUtilisees, NewReglesUtilisees),
        print([R, ":", Conclusions]),
        faits(Conclusions), % j'ajoute ses conclusions.
        doSaturer(NewReglesUtilisees, []);

        (member(R, ReglesUtilisees); not(premissesOk(Premisses))),
        % doSaturer(ReglesUtilisees, NewReglesEssayees)
        findall(_, regle(_,_,_), TRegles),
        length(TRegles, LRegles),
        length(NewReglesEssayees, LNewReglesEssayees),
        LRegles is LNewReglesEssayees,
        true
    ).

saturer() :-
    doSaturer([], []).

% raz.
% faits([a,c,non(d)]).
