# Generated from MiniC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#progRule.
    def visitProgRule(self, ctx:MiniCParser.ProgRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#varDeclList.
    def visitVarDeclList(self, ctx:MiniCParser.VarDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#varDecl.
    def visitVarDecl(self, ctx:MiniCParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#idListBase.
    def visitIdListBase(self, ctx:MiniCParser.IdListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#idList.
    def visitIdList(self, ctx:MiniCParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statList.
    def visitStatList(self, ctx:MiniCParser.StatListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#stat.
    def visitStat(self, ctx:MiniCParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignStat.
    def visitAssignStat(self, ctx:MiniCParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ifStat.
    def visitIfStat(self, ctx:MiniCParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#stat_block.
    def visitStat_block(self, ctx:MiniCParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#whileStat.
    def visitWhileStat(self, ctx:MiniCParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printintStat.
    def visitPrintintStat(self, ctx:MiniCParser.PrintintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printfloatStat.
    def visitPrintfloatStat(self, ctx:MiniCParser.PrintfloatStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printstringStat.
    def visitPrintstringStat(self, ctx:MiniCParser.PrintstringStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exprListEmpty.
    def visitExprListEmpty(self, ctx:MiniCParser.ExprListEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exprListBase.
    def visitExprListBase(self, ctx:MiniCParser.ExprListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exprList.
    def visitExprList(self, ctx:MiniCParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#notExpr.
    def visitNotExpr(self, ctx:MiniCParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MiniCParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#atomExpr.
    def visitAtomExpr(self, ctx:MiniCParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#orExpr.
    def visitOrExpr(self, ctx:MiniCParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniCParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MiniCParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MiniCParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#equalityExpr.
    def visitEqualityExpr(self, ctx:MiniCParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#andExpr.
    def visitAndExpr(self, ctx:MiniCParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parExpr.
    def visitParExpr(self, ctx:MiniCParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#intAtom.
    def visitIntAtom(self, ctx:MiniCParser.IntAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#floatAtom.
    def visitFloatAtom(self, ctx:MiniCParser.FloatAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#booleanAtom.
    def visitBooleanAtom(self, ctx:MiniCParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#idAtom.
    def visitIdAtom(self, ctx:MiniCParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#stringAtom.
    def visitStringAtom(self, ctx:MiniCParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#basicType.
    def visitBasicType(self, ctx:MiniCParser.BasicTypeContext):
        return self.visitChildren(ctx)



del MiniCParser