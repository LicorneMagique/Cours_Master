#!/usr/bin/python3
# -*- coding: utf-8 -*-

import networkx as nx
import graphviz as gz

from .Operands import (Condition, Immediate, Offset,
                      TemporaryPool, Function,
                      A0,
                      ZERO, S, T)
from .Instruction3A import (
    Instruction, Instru3A, Comment, Label
)

"""
MIF08, CAP, CodeGeneration, RiscV API
 Classes for a RiscV program: constructors, allocation, dump.
"""


class RiscVFunction:
    """Representation of a RiscV program (i.e. list of
    instructions)."""

    def __init__(self, name):
        Instruction.count = 0
        self._listIns = []
        self._nbtmp = -1
        self._nblabel = -1
        self._dec = 0
        self._pool = TemporaryPool()
        self._stacksize = 0
        self._name = name
        # CFG Stuff - Lab 5 Only
        self._start = None
        self._end = None
        self._label_div_by_zero = self.new_label("div_by_zero")

    def add_edge(self, src, dest):
        dest._in.append(src)
        src._out.append(dest)

    def add_instruction(self, i, linkwithsucc=True):
        """Utility function to add an instruction in the program.
        in Lab 4, only add at the end of the instruction list (_listIns)
        in Lab 5, will be used to also add in the CFG structure.
        """
        if not self._listIns:  # empty list: empty prg
            self._start = i
        else:
            if self._end is not None:
                self.add_edge(self._end, i)
        self._end = i
        if not linkwithsucc:
            self._end = None
        self._listIns.append(i)
        return i

    def iter_instructions(self, f):
        """Iterate over instructions.

        For each real instruction (not label or comment), call f,
        which must return either None or a list of instruction. If it
        returns None, nothing happens. If it returns a list, then the
        instruction is replaced by this list.

        """
        i = 0
        while i < len(self._listIns):
            old_i = self._listIns[i]
            if not old_i.is_instruction():
                i += 1
                continue
            new_i_list = f(old_i)
            if new_i_list is None:
                i += 1
                continue
            del self._listIns[i]
            self._listIns.insert(i, Comment(str(old_i)))
            i += 1
            for new_i in new_i_list:
                self._listIns.insert(i, new_i)
                i += 1
            self._listIns.insert(i, Comment("end " + str(old_i)))
            i += 1

    def get_instructions(self):
        return self._listIns

    def new_tmp(self):
        """
        Return a new fresh temporary (temp)
        + add in list
        """
        return self._pool.new_tmp()

    def new_offset(self, base):
        """
        Return a new offset in the memory stack
        """
        self._dec = self._dec + 1
        return Offset(base, -8 * self._dec)

    def get_offset(self):
        return self._dec

    def get_stacksize(self):
        return self._stacksize

    def new_label(self, name):
        """
        Return a new label
        """
        self._nblabel = self._nblabel + 1
        return Label(name + "_" + str(self._nblabel) + "_" + self._name)

    def get_label_div_by_zero(self):
        return self._label_div_by_zero

    # each instruction has its own "add in list" version
    def addLabel(self, s):
        return self.add_instruction(s)

    def addComment(self, s):
        self.add_instruction(Comment(s))

    def addInstructionPRINTINT(self, reg):
        """Print integer value, with newline. (see Expand)"""
        # a print instruction generates the temp it prints.
        ins = Instru3A("mv", A0, reg)
        self.add_instruction(ins)
        self.addInstructionCALL('println_int')

    # Other printing instructions are not implemented.

    def addInstructionCALL(self, function):
        if isinstance(function, str):
            function = Function(function)
        assert isinstance(function, Function)
        self.add_instruction(Instru3A('call', function))

    # Unconditional jump to label.
    def addInstructionJUMP(self, label):
        assert isinstance(label, Label)
        i = Instru3A("j", label)
        # add in list but do not link with the following node
        self.add_instruction(i, linkwithsucc=False)
        self.add_edge(i, label)
        return i

    # Conditional jump
    def addInstructionCondJUMP(self, label, op1, c, op2):
        """Add a conditional jump to the code.

        This is a wrapper around bge, bgt, beq, ... c is a Condition, like
        Condition('bgt'), Condition(MiniCParser.EQ), ...
        """
        assert isinstance(label, Label)
        assert isinstance(c, Condition)
        if op2 != 0:
            ins = Instru3A(c.__str__(), op1, op2, label)
        else:
            ins = Instru3A(c.__str__(), op1, ZERO, label)
        self.add_instruction(ins)
        self.add_edge(ins, label)
        return ins

    def addInstructionADD(self, dr, sr1, sr2orimm7):
        if isinstance(sr2orimm7, Immediate):
            ins = Instru3A("addi", dr, sr1, sr2orimm7)
        else:
            ins = Instru3A("add", dr, sr1, sr2orimm7)
        self.add_instruction(ins)

    def addInstructionMUL(self, dr, sr1, sr2orimm7):
        if isinstance(sr2orimm7, Immediate):
            raise MiniCInternalError("Cant multiply by an immediate")
        else:
            ins = Instru3A("mul", dr, sr1, sr2orimm7)
        self.add_instruction(ins)

    def addInstructionDIV(self, dr, sr1, sr2orimm7):
        if isinstance(sr2orimm7, Immediate):
            raise MiniCInternalError("Cant divide by an immediate")
        else:
            ins = Instru3A("div", dr, sr1, sr2orimm7)
        self.add_instruction(ins)

    def addInstructionREM(self, dr, sr1, sr2orimm7):
        if isinstance(sr2orimm7, Immediate):
            raise MiniCInternalError("Cant divide by an immediate")
        else:
            ins = Instru3A("rem", dr, sr1, sr2orimm7)
        self.add_instruction(ins)

    def addInstructionNOT(self, dr, sr):
        ins = Instru3A("not", dr, sr)
        self.add_instruction(ins)

    def addInstructionSUB(self, dr, sr1, sr2orimm7):
        assert not isinstance(sr2orimm7, Immediate)
        ins = Instru3A("sub", dr, sr1, sr2orimm7)
        self.add_instruction(ins)

    def addInstructionAND(self, dr, sr1, sr2orimm7):
        ins = Instru3A("and", dr, sr1, sr2orimm7)
        self.add_instruction(ins)

    def addInstructionOR(self, dr, sr1, sr2orimm7):
        ins = Instru3A("or", dr, sr1, sr2orimm7)
        self.add_instruction(ins)

    # Copy values (immediate or in register)
    def addInstructionLI(self, dr, imm7):
        ins = Instru3A("li", dr, imm7)
        self.add_instruction(ins)

    def addInstructionMV(self, dr, sr):
        ins = Instru3A("mv", dr, sr)
        self.add_instruction(ins)

    def addInstructionLD(self, dr, mem):
        ins = Instru3A("ld", dr, mem)
        self.add_instruction(ins)

    def addInstructionSD(self, sr, mem):
        ins = Instru3A("sd", sr, mem)
        self.add_instruction(ins)

    def printCode(self, output, comment=None):
        # compute size for the local stack - do not forget to align by 16
        fo = self.get_stacksize()  # allocate enough memory for stack
        cardoffset = 8 * (fo + (0 if fo % 2 == 0 else 1)) + 16
        output.write(
            "##Automatically generated RISCV code, MIF08 & CAP\n")
        if comment is not None:
            output.write("##{} version\n".format(comment))
        output.write("\n\n##prelude\n")
        output.write("""
        .text
        .globl {0}
{0}:
        addi sp, sp, -{1}
        sd ra, 0(sp)
        sd fp, 8(sp)
        addi fp, sp, {1}
        """.format(self._name, cardoffset))
        # Stack in RiscV is managed with SP
        output.write("\n\n##Generated Code\n")
        for i in self._listIns:
            i.printIns(output)
        output.write("\n\n##postlude\n")
        output.write("""
        ld ra, 0(sp)
        ld fp, 8(sp)
        addi sp, sp, {0}
        ret

{1}:
        la a0, {1}_msg
        call println_string
        li a0, 1
        call exit
{1}_msg: .string "Division by 0"

""".format(cardoffset, self._label_div_by_zero))

    def printDot(self, filename, view=False):
        # Only used in Lab 5
        graph = nx.DiGraph()
        names = dict()
        for i, instruction in enumerate(self._listIns):
            names[instruction] = str(i) + "_" + str(instruction)
        # nodes
        for instruction in self._listIns:
            graph.add_node(names[instruction])
        # edges
        for instruction in self._listIns:
            for child in instruction._out:
                graph.add_edge(names[instruction], names[child])
        # Add a fake "START" node to mark the entry of the CFG
        if i == 0:
            graph.add_node("START")
            graph.add_edge("START", names[self._start])
        graph.graph['graph'] = dict()
        graph.graph['graph']['overlap'] = 'false'
        nx.drawing.nx_agraph.write_dot(graph, filename)
        gz.render('dot', 'pdf', filename)
        if view:
            gz.view(filename + '.pdf')
