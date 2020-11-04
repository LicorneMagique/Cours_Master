# LAB2, arithmetic expressions interpreter
MIF08, 2020-2021, Laure Gonnord & Matthieu Moy

# Content

This directory contains an interpreter for simple arithmetic
expressions like 5+3, for instance. The intepreter evaluates the
arithmetic expressions and prints their value on the standard
output.

# Usage

* `make` to generate Arit1Lexer.py and Arit1Parser.py (once)

* `python3 arit1.py <path/and/test/name>` to test a given file, for
 instance: 
 `python3 arit1.py testfiles/test01.txt`  should print `1+2 = 3`

* `make tests` to test on all tests files of the `testfile` directory

# Syntax of our language/restrictions

The syntax is the one textually given in the Lab2 sheet. 
Restriction : we did not implement minus nor unary minus.

# Design choices

TODO

# Known bugs

N/A
