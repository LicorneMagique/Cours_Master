# MiniC Compiler 
LAB4 (simple code generation), MIF08 / CAP 2020-21

# Authors

YOUR NAME HERE

# Contents

TODO for STUDENTS : Say a bit about the code infrastructure ...

# Howto

`make run-trace ALLOC=naive TESTFILE=TP04/tests/provided/step1/test00.c`: launch the compiler, then the RISCV assembler and simulators to run a single file. In this example, should print 42.

`make tests-codegen` to launch the testsuite.

# Test design 

TODO: explain your tests

# Design choices

TODO: explain your choices

# Known bugs

TODO: Bugs and limitations.

# Checklists

A check ([X]) means that the feature is implemented 
and *tested* with appropriate test cases.

## Code generation

- [ ] Number Atom 
- [ ] Boolean Atom
- [ ] Id Atom 
- [ ] Additive expression
- [ ] Multiplicative expr
- [ ] UnaryMinus expr
- [ ] Or expression
- [ ] And expression
- [ ] Equality expression
- [ ] Relational expression (! many cases -> many tests)
- [ ] Not expression

## Statements

- [ ] Prog, assignements
- [ ] While
- [ ] Cond Block
- [ ] If
- [ ] Nested ifs
- [ ] Nested whiles

## Allocation

- [ ] Naive allocation
- [ ] All in memory allocation
- [ ] Massive tests of memory allocation

