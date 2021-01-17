# MiniC interpreter and typer

LAB3, MIF08 / CAP 2020-21

## Authors

Julien GIRAUD

## Contents

Tout ce qui suit concerne le fichier `MiniCInterpretVisitor.py`

- J'ai rajouté la fonction `declVar` pour éviter la redondance de code des fonctions `visitVarDecl` et `visitVaDeclList`

- J'ai traité des cas d'erreur qui ne devraient jamais arriver

## Howto

`make run-interpreter TESTFILE=TP03/tests/provided/examples/test00.c` for a single run
it should print 42

`make tests` to test all the files in `*/tests/*` according to `EXPECTED` results.

You can select the files you want to test by using `make TEST_FILES='TP03/**/*bad*.c'` (`**` means
"any number of possibly nested directories").

## Test design

Mes tests ont pour objectif de tester tout ce que j'ai implémenté qui n'était pas déjà testé

## Design choices

J'ai fait le choix de suivre le code existant :-)

## Known bugs

Pas à ma connaissance, je n'ai donc probablement pas assez testé
