# Generated from Arit.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\7")
        buf.write("\13\66\n\13\f\13\16\139\13\13\3\f\6\f<\n\f\r\f\16\f=\3")
        buf.write("\r\3\r\7\rB\n\r\f\r\16\rE\13\r\3\r\3\r\3\16\5\16J\n\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\6\17Q\n\17\r\17\16\17R\3\17")
        buf.write("\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\3\2\7\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\3\2\62;\4\2\f\f\17\17\4\2\13\13\"\"\2Z\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\3\37\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2")
        buf.write("\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61")
        buf.write("\3\2\2\2\25\63\3\2\2\2\27;\3\2\2\2\31?\3\2\2\2\33I\3\2")
        buf.write("\2\2\35P\3\2\2\2\37 \7u\2\2 !\7g\2\2!\"\7v\2\2\"\4\3\2")
        buf.write("\2\2#$\7?\2\2$\6\3\2\2\2%&\7*\2\2&\b\3\2\2\2\'(\7+\2\2")
        buf.write("(\n\3\2\2\2)*\7=\2\2*\f\3\2\2\2+,\7-\2\2,\16\3\2\2\2-")
        buf.write(".\7/\2\2.\20\3\2\2\2/\60\7,\2\2\60\22\3\2\2\2\61\62\7")
        buf.write("\61\2\2\62\24\3\2\2\2\63\67\t\2\2\2\64\66\t\3\2\2\65\64")
        buf.write("\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\26\3\2")
        buf.write("\2\29\67\3\2\2\2:<\t\4\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2")
        buf.write("\2=>\3\2\2\2>\30\3\2\2\2?C\7%\2\2@B\n\5\2\2A@\3\2\2\2")
        buf.write("BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2\2FG\b")
        buf.write("\r\2\2G\32\3\2\2\2HJ\7\17\2\2IH\3\2\2\2IJ\3\2\2\2JK\3")
        buf.write("\2\2\2KL\7\f\2\2LM\3\2\2\2MN\b\16\2\2N\34\3\2\2\2OQ\t")
        buf.write("\6\2\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2")
        buf.write("\2TU\b\17\2\2U\36\3\2\2\2\b\2\67=CIR\3\b\2\2")
        return buf.getvalue()


class AritLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SCOL = 5
    PLUS = 6
    MINUS = 7
    MULT = 8
    DIV = 9
    ID = 10
    INT = 11
    COMMENT = 12
    NEWLINE = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'set'", "'='", "'('", "')'", "';'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "SCOL", "PLUS", "MINUS", "MULT", "DIV", "ID", "INT", "COMMENT", 
            "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SCOL", "PLUS", "MINUS", 
                  "MULT", "DIV", "ID", "INT", "COMMENT", "NEWLINE", "WS" ]

    grammarFileName = "Arit.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


