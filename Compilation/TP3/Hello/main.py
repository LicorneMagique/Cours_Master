from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from HelloLexer import HelloLexer
from HelloListener import HelloListener
from HelloParser import HelloParser
from antlr4.error.ErrorListener import ErrorListener

import sys

# cf
# https://stackoverflow.com/questions/32224980/python-2-7-antlr4-make-antlr-throw-exceptions-on-invalid-input


class MyErrorListener(ErrorListener):
    """Error listener: methods below will be called by ANTLR when an error
    is raised. If this class is not provided, ANTLR's default error
    management is done."""

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax Error at line " + str(line) + " : " + msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex,
                        exact, ambigAlts, configs):
        raise Exception("Oh no!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex,
                                    stopIndex, conflictingAlts, configs):
        raise Exception("Oh no!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex,
                                 stopIndex, prediction, configs):
        raise Exception("Oh no!!")


class HelloPrintListener(HelloListener):
    """Listener for the parse tree. This class contains one method per
    grammar rule. Methods are called while traversing the tree
    whenever the corresponding node is encountered.
    """

    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())


def main():
    # Setup: read from stdin, instanciate parser
    lexer = HelloLexer(InputStream(sys.stdin.read()))
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    parser._listeners = [MyErrorListener()]  # handling excep

    # Actual parsing
    try:
        tree = parser.hi()
    except Exception as e:
        print(e)
        sys.exit(42)

    print("Parsing completed, now launching the listener.")

    # Tree traversal
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
