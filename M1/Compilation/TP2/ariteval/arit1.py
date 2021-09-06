#! /usr/bin/env python3
"""
Usage:
    python3 arit1.py <filename>
"""
# Main file for MIF08 - Lab02 - 2018-19

from Arit1Lexer import Arit1Lexer
from Arit1Parser import Arit1Parser
from antlr4 import FileStream, CommonTokenStream, StdinStream

# example of arithmetic eval with semantic actions

import argparse


def main(inputname):
    if inputname is None:
        lexer = Arit1Lexer(StdinStream())
    else:
        lexer = Arit1Lexer(FileStream(inputname))
    stream = CommonTokenStream(lexer)
    parser = Arit1Parser(stream)
    parser.prog()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AritEval demo')
    parser.add_argument('filename', type=str, nargs='?',
                        help='Source file.')
    args = parser.parse_args()
    main(args.filename)
