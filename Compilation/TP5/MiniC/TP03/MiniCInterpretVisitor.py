# Visitor to *interpret* MiniC files
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Errors import MiniCRuntimeError, MiniCInternalError

class MiniCInterpretVisitor(MiniCVisitor):

    def __init__(self):
        self._memory = dict()  # store all variable ids and values.
        self.has_main = False

    # visitors for variable declarations

    def visitVarDecl(self, ctx):
        # Initialise all variables in self._memory (toto |-> None)
        # vardecl: typee id_l SCOL
        type = ctx.typee().getText()
        nom = ctx.id_l().getText()
        if not nom in self._memory:
            val = None
            if type == "int":
                val = 0
            elif type == "float":
                val = .0
            elif type == "bool":
                val = False
            elif val == "string":
                val = ""
            self._memory[nom] = val
        else:
            raise MiniCInternalError(
                "Identifier '%s' already declared" % nom
            )

    def visitIdList(self, ctx):
        raise NotImplementedError()

    def visitIdListBase(self, ctx):
        return [ctx.ID().getText()]

    # visitors for atoms --> value
    # this code is given to students except for idatoms !

    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx):
        return int(ctx.getText())

    def visitFloatAtom(self, ctx):
        return float(ctx.getText())

    def visitBooleanAtom(self, ctx):
        return ctx.getText() == "true"

    def visitIdAtom(self, ctx):
        nom = ctx.ID().getText()
        if nom in self._memory:
            return self._memory[nom]
        else:
            raise MiniCInternalError(
                "Unknown identifier '%s' in visitIdAtom" % nom
            )

    def visitStringAtom(self, ctx):
        return ctx.getText()[1:-1]

    # visit expressions
    # this code is given to students
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval | rval

    def visitAndExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval & rval

    def visitEqualityExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        # be careful for float equality
        if ctx.myop.type == MiniCParser.EQ:
            return lval == rval
        else:
            return lval != rval

    def visitRelationalExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.LT:
            return lval < rval
        elif ctx.myop.type == MiniCParser.LTEQ:
            return lval <= rval
        elif ctx.myop.type == MiniCParser.GT:
            return lval > rval
        elif ctx.myop.type == MiniCParser.GTEQ:
            return lval >= rval
        else:
            raise MiniCInternalError(
                "Unknown comparison operator '%s'" % ctx.myop
            )

    def visitAdditiveExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.PLUS:
            if any(isinstance(x, str) for x in (lval, rval)):
                return '{}{}'.format(lval, rval)
            else:
                return lval + rval
        elif ctx.myop.type == MiniCParser.MINUS:
            return lval - rval
        else:
            raise MiniCInternalError(
                "Unknown additive operator '%s'" % ctx.myop)

    def visitMultiplicativeExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.MULT:
            return lval * rval
        elif ctx.myop.type == MiniCParser.DIV:
            if rval == 0:
                raise MiniCRuntimeError("Division by 0")
            if isinstance(lval, int):
                return lval // rval
            else:
                return lval / rval
        elif ctx.myop.type == MiniCParser.MOD:
            return lval % rval
        else:
            raise MiniCInternalError(
                "Unknown multiplication operator '%s'" % ctx.myop)

    def visitNotExpr(self, ctx):
        return not self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx):
        return -self.visit(ctx.expr())

    # visit statements

    def visitPrintintStat(self, ctx):
        val = self.visit(ctx.expr())
        if isinstance(val, bool):
            val = '1' if val else '0'
        print(val)

    def visitPrintfloatStat(self, ctx):
        val = self.visit(ctx.expr())
        if isinstance(val, float):
            val = "%.2f" % val
        print(val)

    def visitPrintstringStat(self, ctx):
        val = self.visit(ctx.expr())
        print(val)

    def visitAssignStat(self, ctx):
        val = self.visit(ctx.expr())
        nom = ctx.ID().getText()
        if nom in self._memory:
            self._memory[nom] = val
        else:
            raise MiniCInternalError(la
                "Unknown identifier '%s' in visitAssignStat" % nom
            )

    def visitIfStat(self, ctx):
        # IF OPAR expr CPAR then_block=stat_block (ELSE else_block=stat_block)?
        # raise NotImplementedError()
        if self.visit(ctx.expr()):
            self.visit(ctx.then_block)
        elif ctx.else_block is not None:
            self.visit(ctx.else_block)

    def visitWhileStat(self, ctx):
        raise NotImplementedError()

    # TOPLEVEL
    def visitProgRule(self, ctx):
        self.visitChildren(ctx)
        if not self.has_main:
            # A program without a main function is compilable (hence
            # it's not a typing error per se), but not executable,
            # hence we consider it a runtime error.
            raise MiniCRuntimeError("No main function in file")
        return

    # Visit a function: ignore if non main!
    def visitFuncDecl(self, ctx):
        funname = ctx.ID().getText()
        if funname == "main":
            self.has_main = True
            self.visit(ctx.vardecl_l())
            self.visit(ctx.block())
