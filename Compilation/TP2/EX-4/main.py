from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from ParenthesesLexer import ParenthesesLexer
from ParenthesesParser import ParenthesesParser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = ParenthesesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ParenthesesParser(stream)
    parser.r()
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
