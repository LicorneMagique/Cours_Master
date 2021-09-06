from .Operands import (Operand, Immediate)

"""
MIF08, CAP, API RiscV. 3A instruction constructors.
This file has no TODO for lab4,
and one TODO for Lab5: dataflow analysis.
"""


def regset_to_string(registerset):
    """Utilitary function: pretty-prints a set of locations."""
    return "{" + ",".join(str(x) for x in registerset) + "}"


class Instruction:
    """Real instruction, comment or label."""
    def __init__(self):
        self._ins = None

        # for liveness dataflow analysis (Lab 5)
        self._in = []
        self._out = []
        self._gen = set()
        self._kill = set()

    def is_instruction(self):
        """True if the object is a true instruction (not a label or
        comment)."""
        return False

    def print_gen_kill(self, i):
        print("instr " + str(i) + ": " + str(self))
        print("gen: " + regset_to_string(self._gen))
        print("kill: " + regset_to_string(self._kill) + "\n")

    def dataflow_one_step(self, mapin, mapout):
        """propagate dataflow information: update _gen and _kill sets
        (mapin,mapout).
        """
        # Reminder: '|' is set union, '-' is subtraction.
        mapout[self] = set()
        for child in self._out:
            mapout[self] = mapout[self] | mapin[child]

        mapin[self] = (mapout[self] - self._kill) | self._gen


class Instru3A(Instruction):

    def __init__(self, ins, arg1=None, arg2=None, arg3=None, args=None):
        # A regular 3-address instruction has <=3 args, but compJUMP has 4.
        super().__init__()
        self._ins = ins
        if args:
            self.args = args
        else:
            self.args = [arg for arg in (arg1, arg2, arg3) if arg is not None]
        args = self.args
        for i in range(len(args)):
            if isinstance(args[i], int):
                args[i] = Immediate(args[i])
            assert isinstance(args[i], Operand), (args[i], type(args[i]))

    def is_instruction(self):
        """True if the object is a true instruction (not a label or
        comment)."""
        return True

    def get_name(self):
        # convention is to use lower-case in RISCV, even though not strictly necessary
        return self._ins.lower()

    def is_read_only(self):
        """True if the instruction only reads from its operands.

        Otherwise, the first operand is considered as the destination
        and others are source.
        """
        return (self.get_name().startswith("b")
                or self.get_name() == "jump_cond"  # meta-instruction
                or self.get_name() == "j"
                or self.get_name() == "ld"
                or self.get_name() == "lw"
                or self.get_name() == "lb")

    def __str__(self):
        s = self._ins
        first = True
        for arg in self.args:
            if first:
                s += ' ' + str(arg)
                first = False
            else:
                s += ', ' + str(arg)
        return s

    def printIns(self, stream):
        """Print the instruction on the output."""
        print('       ', str(self), file=stream)

    def unfold(self):
        """Utility function to get both the instruction name and the operands
        in one call. Example:

        ins, args = i.unfold()
        """
        return self.get_name(), self.args


class Label(Instruction, Operand):
    """ A label is here a regular instruction"""

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    def __str__(self):
        return ("lbl_{}".format(self._name))

    def printIns(self, stream):
        print(str(self) + ':', file=stream)


class Comment(Instruction):
    """ A comment is here a regular instruction"""

    def __init__(self, content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._content = content

    def __str__(self):  # use only for printDot !
        return "comment"

    def printIns(self, stream):
        print('        # ' + self._content, file=stream)
