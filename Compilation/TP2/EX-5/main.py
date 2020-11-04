from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from Ex5Lexer import Ex5Lexer
from Ex5Parser import Ex5Parser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = Ex5Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Ex5Parser(stream)
    parser.start()
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
