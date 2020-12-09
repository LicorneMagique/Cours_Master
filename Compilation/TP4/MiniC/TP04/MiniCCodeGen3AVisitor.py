from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from .APIRiscV import (RiscVFunction, Condition)
from .Instruction3A import Label
from . import Operands
from antlr4.tree.Trees import Trees
from Errors import MiniCInternalError, MiniCUnsupportedError

"""
CAP, MIF08, three-address code generation + simple alloc
This visitor constructs an object of type "RiscVFunction".
"""


class MiniCCodeGen3AVisitor(MiniCVisitor):

    def __init__(self, debug, parser):
        super().__init__()
        self._parser = parser
        self._debug = debug
        self._functions = []
        self._current_function = None
        self._lastlabel = ""
        self.ctx_stack = []  # useful for nested ITE

    def get_functions(self):
        return self._functions

    def printSymbolTable(self):
        print("--variables to temporaries map--")
        for keys, values in self._symbol_table.items():
            print(keys + '-->' + str(values))

    # handle variable decl

    def visitVarDecl(self, ctx):
        type_str = ctx.typee().getText()
        vars_l = self.visit(ctx.id_l())
        for name in vars_l:
            if name in self._symbol_table:
                raise MiniCInternalError(
                    "Variable {} has already been declared".format(name))
            else:
                tmp = self._current_function.new_tmp()
                self._symbol_table[name] = tmp
                if type_str not in ("int", "bool"):
                    raise MiniCUnsupportedError("Unsupported type " + type_str)
                # Initialization to 0 or False, both represented with 0
                self._current_function.addInstructionLI(tmp, 0)

    def visitIdList(self, ctx):
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx):
        return [ctx.ID().getText()]

    # expressions

    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx):
        val = int(ctx.getText())
        dest_temp = self._current_function.new_tmp()
        self._current_function.addInstructionLI(dest_temp, val)
        return dest_temp

    def visitFloatAtom(self, ctx):
        raise MiniCUnsupportedError("float literal")

    def visitBooleanAtom(self, ctx):
        # true is 1 false is 0
        raise NotImplementedError()

    def visitIdAtom(self, ctx):
        try:
            # get the temporary associated to id
            return self._symbol_table[ctx.getText()]
        except KeyError:
            raise MiniCInternalError(
                "Undefined variable {}, this should have failed to typecheck."
                .format(ctx.getText())
            )

    def visitStringAtom(self, ctx):
        raise MiniCUnsupportedError("string atom")

    # now visit expressions : TODO

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitAdditiveExpr(self, ctx):
        raise NotImplementedError()

    def visitOrExpr(self, ctx):
        raise NotImplementedError()

    def visitAndExpr(self, ctx):
        raise NotImplementedError()

    def visitEqualityExpr(self, ctx):
        return self.visitRelationalExpr(ctx)

    def visitRelationalExpr(self, ctx):
        c = Condition(ctx.myop.type)
        if self._debug:
            print("relational expression:")
            print(Trees.toStringTree(ctx, None, self._parser))
            print("Condition:", c)
        raise NotImplementedError()

    def visitMultiplicativeExpr(self, ctx):
        div_by_zero_lbl = self._current_function.get_label_div_by_zero()
        raise NotImplementedError()

    def visitNotExpr(self, ctx):
        raise NotImplementedError()

    def visitUnaryMinusExpr(self, ctx):
        raise NotImplementedError("unaryminusexpr")

    def visitProgRule(self, ctx):
        self.visitChildren(ctx)
        return

    def visitFuncDecl(self, ctx):
        funcname = ctx.ID().getText()
        self._current_function = RiscVFunction(funcname)
        self._symbol_table = dict()

        self.visit(ctx.vardecl_l())
        self.visit(ctx.block())
        self._current_function.addComment("Return at end of function:")
        # TODO: at some point there will be a non harcoded return value
        # TODO: for functions, but for now, "return 0".
        self._current_function.addInstructionLI(Operands.A0, 0)
        self._functions.append(self._current_function)

        # We don't need to bother with div_by_zero in our CFG, hence remove it
        # if it was added.
        div_0_label = self._current_function.get_label_div_by_zero()
        for jump in div_0_label._in:
            jump._out.remove(div_0_label)
        div_0_label._in = []

        self._current_function = None

    def visitAssignStat(self, ctx):
        if self._debug:
            print("assign statement, rightexpression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        expr_temp = self.visit(ctx.expr())
        name = ctx.ID().getText()
        self._current_function.addInstructionMV(self._symbol_table[name], expr_temp)

    def visitIfStat(self, ctx):
        if self._debug:
            print("if statement")
        # invent a new label, then push in the label stack
        end_if_label = self._current_function.new_label("end_if")
        raise NotImplementedError()
        self._current_function.addLabel(end_if_label)


    def visitWhileStat(self, ctx):
        if self._debug:
            print("while statement, condition is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
            print("and block is:")
            print(Trees.toStringTree(ctx.stat_block(), None, self._parser))
        raise NotImplementedError()
    # visit statements

    def visitPrintintStat(self, ctx):
        expr_loc = self.visit(ctx.expr())
        if self._debug:
            print("print_int statement, expression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        self._current_function.addInstructionPRINTINT(expr_loc)

    def visitPrintfloatStat(self, ctx):
        raise MiniCUnsupportedError("print_float")

    def visitPrintstringStat(self, ctx):
        raise MiniCUnsupportedError("Unsupported type string")

    def visitStatList(self, ctx):
        for stat in ctx.stat():
            self._current_function.addComment(Trees.toStringTree(stat, None, self._parser))
            self.visit(stat)

    def visitForForStat(self, ctx):
        raise NotImplementedError("fortran for")

    def visitArrayAllocExpr(self, ctx):
        raise NotImplementedError("array")

    def visitArrayReadExpr(self, ctx):
        raise NotImplementedError("array")

    def visitArrayWriteStat(self, ctx):
        raise NotImplementedError("array")

    def visitArrayType(self, ctx):
        raise NotImplementedError("array")
