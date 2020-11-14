from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Errors import MiniCInternalError

from enum import Enum


class MiniCTypeError(Exception):
    pass


class BaseType(Enum):
    Float, Integer, Boolean, String = range(4)


# Basic Type Checking for MiniC programs.
class MiniCTypingVisitor(MiniCVisitor):

    def __init__(self):
        self._memorytypes = dict()  # id-> types
        self._current_function = "main"

    def _raise(self, ctx, for_what, *types):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: invalid type for {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, for_what,
                ' and '.join(t.name.lower() for t in types)))

    def _raiseMismatch(self, ctx, for_what, *types):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: type mismatch for {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, for_what,
                ' and '.join(t.name.lower() for t in types)))

    def _raiseNonType(self, ctx, message):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, message))

    # type declaration

    def visitVarDecl(self, ctx):
        vars_l = self.visit(ctx.id_l())
        tt = self.visit(ctx.typee())
        for name in vars_l:
            if name in self._memorytypes:
                self._raiseNonType(ctx,
                                   "Variable {0} already declared".
                                   format(name))
            self._memorytypes[name] = tt
        return

    def visitBasicType(self, ctx):
        if ctx.mytype.type == MiniCParser.INTTYPE:
            return BaseType.Integer
        elif ctx.mytype.type == MiniCParser.FLOATTYPE:
            return BaseType.Float
        elif ctx.mytype.type == MiniCParser.BOOLTYPE:
            return BaseType.Boolean
        elif ctx.mytype.type == MiniCParser.STRINGTYPE:
            return BaseType.String
        else:
            raise MiniCInternalError("Type not implemented")

    def visitIdList(self, ctx):
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx):
        return [ctx.ID().getText()]

    # typing visitors for expressions, statements !

    # visitors for atoms --> value
    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx):
        return BaseType.Integer

    def visitFloatAtom(self, ctx):
        return BaseType.Float

    def visitBooleanAtom(self, ctx):
        return BaseType.Boolean

    def visitIdAtom(self, ctx):
        try:
            valtype = self._memorytypes[ctx.getText()]
            return valtype
        except KeyError:
            self._raiseNonType(ctx,
                               "Undefined variable {}".format(ctx.getText()))

    def visitStringAtom(self, ctx):
        return BaseType.String

    # now visit expr

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if (BaseType.Boolean == lvaltype) and (BaseType.Boolean == rvaltype):
            return BaseType.Boolean
        else:
            self._raise(ctx, 'boolean operands', lvaltype, rvaltype)

    def visitAndExpr(self, ctx):
        return self.visitOrExpr(ctx)  # Same typing rules

    def visitEqualityExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raiseMismatch(ctx, 'equality operands', lvaltype, rvaltype)

        return BaseType.Boolean

    def visitRelationalExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raise(ctx, 'relational operands', lvaltype, rvaltype)

        if lvaltype not in (BaseType.Integer, BaseType.Float):
            self._raise(ctx, 'relational operands', lvaltype, rvaltype)

        return BaseType.Boolean

    def visitAdditiveExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raise(ctx, 'additive operands', lvaltype, rvaltype)
        if lvaltype not in (BaseType.Integer, BaseType.Float, BaseType.String):
            self._raise(ctx, 'additive operands', lvaltype, rvaltype)
        if ctx.myop.type != MiniCParser.PLUS and lvaltype == BaseType.String:
            self._raise(ctx, 'additive operands', lvaltype, rvaltype)

        return lvaltype

    def visitMultiplicativeExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raise(ctx, 'multiplicative operands', lvaltype, rvaltype)

        if lvaltype not in (BaseType.Integer, BaseType.Float):
            self._raise(ctx, 'multiplicative operands', lvaltype, rvaltype)

        return lvaltype

    def visitNotExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Boolean:
            self._raise(ctx, 'not expression', etype)
        else:
            return BaseType.Boolean

    def visitUnaryMinusExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if etype not in (BaseType.Integer, BaseType.Float):
            self._raise(ctx, 'unary minus operand', etype)

        return etype

    # visit statements

    def visitPrintintStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype not in (BaseType.Integer, BaseType.Boolean):
            self._raise(ctx, 'println_int statement', etype)

    def visitPrintfloatStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Float:
            self._raise(ctx, 'println_float statement', etype)

    def visitPrintstringStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.String:
            self._raise(ctx, 'println_string statement', etype)

    def visitAssignStat(self, ctx):
        valtype = self.visit(ctx.expr())
        name = ctx.ID().getText()
        if name not in self._memorytypes:
            self._raiseNonType(
                ctx, "Undefined variable "+name)
        if self._memorytypes[name] != valtype:
            self._raiseMismatch(
                ctx, name, self._memorytypes[name], valtype)

    def visitWhileStat(self, ctx):
        condtype = self.visit(ctx.expr())
        if condtype != BaseType.Boolean:
            self._raise(ctx, 'while condition', condtype)
        self.visit(ctx.stat_block())

    def visitIfStat(self, ctx):
        condtype = self.visit(ctx.expr())
        if condtype != BaseType.Boolean:
            self._raise(ctx, 'if condition', condtype)
        self.visit(ctx.then_block)
        if ctx.else_block is not None:
            self.visit(ctx.else_block)
