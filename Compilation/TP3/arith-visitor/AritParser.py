# Generated from Arit.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\33\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4&\n\4")
        buf.write("\f\4\16\4)\13\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\61\n\5\3\5")
        buf.write("\2\3\6\6\2\4\6\b\2\4\3\2\n\13\3\2\b\t\2\64\2\13\3\2\2")
        buf.write("\2\4\32\3\2\2\2\6\34\3\2\2\2\b\60\3\2\2\2\n\f\5\4\3\2")
        buf.write("\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16")
        buf.write("\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22\5\6\4\2\22")
        buf.write("\23\7\7\2\2\23\33\3\2\2\2\24\25\7\3\2\2\25\26\7\f\2\2")
        buf.write("\26\27\7\4\2\2\27\30\5\6\4\2\30\31\7\7\2\2\31\33\3\2\2")
        buf.write("\2\32\21\3\2\2\2\32\24\3\2\2\2\33\5\3\2\2\2\34\35\b\4")
        buf.write("\1\2\35\36\5\b\5\2\36\'\3\2\2\2\37 \f\5\2\2 !\t\2\2\2")
        buf.write("!&\5\6\4\6\"#\f\4\2\2#$\t\3\2\2$&\5\6\4\5%\37\3\2\2\2")
        buf.write("%\"\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\7\3\2\2\2")
        buf.write(")\'\3\2\2\2*\61\7\r\2\2+\61\7\f\2\2,-\7\5\2\2-.\5\6\4")
        buf.write("\2./\7\6\2\2/\61\3\2\2\2\60*\3\2\2\2\60+\3\2\2\2\60,\3")
        buf.write("\2\2\2\61\t\3\2\2\2\7\r\32%\'\60")
        return buf.getvalue()


class AritParser ( Parser ):

    grammarFileName = "Arit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'set'", "'='", "'('", "')'", "';'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SCOL", "PLUS", "MINUS", "MULT", "DIV", 
                      "ID", "INT", "COMMENT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_atom = 3

    ruleNames =  [ "prog", "statement", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SCOL=5
    PLUS=6
    MINUS=7
    MULT=8
    DIV=9
    ID=10
    INT=11
    COMMENT=12
    NEWLINE=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StatementListContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(AritParser.EOF, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.StatementContext)
            else:
                return self.getTypedRuleContext(AritParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = AritParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            localctx = AritParser.StatementListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AritParser.T__0) | (1 << AritParser.T__2) | (1 << AritParser.ID) | (1 << AritParser.INT))) != 0)):
                    break

            self.state = 13
            self.match(AritParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprInstrContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def SCOL(self):
            return self.getToken(AritParser.SCOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprInstr" ):
                listener.enterExprInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprInstr" ):
                listener.exitExprInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprInstr" ):
                return visitor.visitExprInstr(self)
            else:
                return visitor.visitChildren(self)


    class AssignInstrContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AritParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def SCOL(self):
            return self.getToken(AritParser.SCOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignInstr" ):
                listener.enterAssignInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignInstr" ):
                listener.exitAssignInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignInstr" ):
                return visitor.visitAssignInstr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = AritParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AritParser.T__2, AritParser.ID, AritParser.INT]:
                localctx = AritParser.ExprInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(AritParser.SCOL)
                pass
            elif token in [AritParser.T__0]:
                localctx = AritParser.AssignInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(AritParser.T__0)
                self.state = 19
                self.match(AritParser.ID)
                self.state = 20
                self.match(AritParser.T__1)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(AritParser.SCOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.mdop = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.ExprContext)
            else:
                return self.getTypedRuleContext(AritParser.ExprContext,i)

        def MULT(self):
            return self.getToken(AritParser.MULT, 0)
        def DIV(self):
            return self.getToken(AritParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpr" ):
                return visitor.visitMultiplicationExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(AritParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.pmop = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.ExprContext)
            else:
                return self.getTypedRuleContext(AritParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(AritParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(AritParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AritParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AritParser.AtomExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 27
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = AritParser.MultiplicationExprContext(self, AritParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        localctx.mdop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==AritParser.MULT or _la==AritParser.DIV):
                            localctx.mdop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = AritParser.AdditiveExprContext(self, AritParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 33
                        localctx.pmop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==AritParser.PLUS or _la==AritParser.MINUS):
                            localctx.pmop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expr(3)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AritParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdAtom" ):
                listener.enterIdAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdAtom" ):
                listener.exitIdAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdAtom" ):
                return visitor.visitIdAtom(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AritParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = AritParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AritParser.INT]:
                localctx = AritParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(AritParser.INT)
                pass
            elif token in [AritParser.ID]:
                localctx = AritParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(AritParser.ID)
                pass
            elif token in [AritParser.T__2]:
                localctx = AritParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(AritParser.T__2)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(AritParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




