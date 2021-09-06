# LAB2, arithmetic expressions interpreter

MIF08, 2020-2021, Laure Gonnord & Matthieu Moy

**Julien Giraud** P1704709

---

## Content

This directory contains an interpreter for simple arithmetic
expressions like 5+3, for instance. The intepreter evaluates the
arithmetic expressions and prints their value on the standard
output.

## Usage

* `make` to generate Arit1Lexer.py and Arit1Parser.py (once)

* `python3 arit1.py <path/and/test/name>` to test a given file, for instance:  
 `python3 arit1.py testfiles/test01.txt` should print `1+2 = 3`

* `make tests` to test on all tests files of the `testfile` directory

## Syntax of our language/restrictions

The syntax is the one textually given in the Lab2 sheet.  
Restriction : we did not implement minus nor unary minus.

## Design choices

* We can use MINUS before an expression (unary MINUS operator)
* We can use MINUS between two expressions (binary MINUS operator)
* Binary MINUS operator has priority over unary MINUS operator
* MINUS operator has priority over PLUS operator
* MULT operator has priority over MINUS operator

## Known bugs

I guess I haven't tested enough because I haven't found any bugs 😅
