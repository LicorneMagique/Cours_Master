from TP04.Operands import Temporary, S, Register, GP_REGS, Offset, FP
from TP04.Instruction3A import Instru3A, regset_to_string
from .LibGraphes import Graph  # For Graph coloring utility functions
from Errors import MiniCInternalError

import copy

"""
MIF08, CAP, 2020-2021
Allocation "replace" functions for direct code generation.
Each function suppose that its corresponding alloc has been called before.
"""


def replace_reg(old_i):
    """Replace Temporary operands with
    the corresponding allocated register."""
    ins, old_args = old_i.unfold()
    args = []
    for arg in old_args:
        if isinstance(arg, Temporary):
            arg = arg.get_alloced_loc()
        args.append(arg)
    return [Instru3A(ins, args=args)]


def replace_mem(old_i):
    """Replace Temporary operands with the corresponding allocated
    memory location. FP points to the stack"""
    before = []
    after = []
    ins, old_args = old_i.unfold()
    args = []
    numreg = 8
    # TODO (lab4): compute before,after,args.
    for arg in old_args:
        if isinstance(arg, Temporary):
            reg = GP_REGS[numreg]
            operand = arg.get_alloced_loc()
            before.append(Instru3A("ld", reg, operand))
            args.append(reg)
            after.append(Instru3A("sd", reg, operand))
            numreg += 1
        else:
            args.append(arg)
    i = Instru3A(ins, args=args)
    return before + [i] + after


def replace_smart(old_i):
    """Replace Temporary operands with the corresponding allocated
    physical register OR memory location."""
    before = []
    after = []
    ins, old_args = old_i.unfold()
    args = []
    # TODO (lab5): compute before,after,args. This is a superset of what
    # TODO (lab5): replace_mem does.
    # and now return the new list!
    i = Instru3A(ins, args=args)  # change argument list into args
    return before + [i] + after


class AllocationError(Exception):
    """
    Useful to properly launch an error!
    """

    def __init__(self, msg):
        super().__init__(msg)


class Allocator():
    def __init__(self, function):
        self._f = function

    def run(self):
        pass


class NaiveAllocator(Allocator):
    def __init__(self, *args):
        super().__init__(*args)

    # Allocation functions
    def run(self):
        """ Allocate all temporaries to registers.
        Fail if there are too many temporaries."""
        regs = list(GP_REGS)  # Get a writable copy
        temp_allocation = dict()
        for tmp in self._f._pool._all_temps:
            try:
                reg = regs.pop()
            except IndexError:
                raise AllocationError(
                    "Too many temporaries ({}) for the naive allocation, sorry."
                    .format(len(self._f._pool._all_temps)))
            temp_allocation[tmp] = reg
        self._f._pool.set_temp_allocation(temp_allocation)
        self._f.iter_instructions(replace_reg)


class AllInMemAllocator(Allocator):
    def __init__(self, *args):
        super().__init__(*args)

    def run(self):
        """Allocate all temporaries to memory. Hypothesis:
        - Expanded instructions can use  s2 and
        s3 (to store the values of temporaries before the actual
        instruction).
        """
        self._f._pool.set_temp_allocation(
            {temp: self._f.new_offset(FP) for temp in self._f._pool._all_temps})
        self._f._stacksize = self._f.get_offset()
        self._f.iter_instructions(replace_mem)


class SmartAllocator(Allocator):
    def __init__(self, function, basename, debug=False, debug_graphs=False, *args):
        self._basename = basename
        self._debug = debug
        self._debug_graphs = debug_graphs
        self._mapin = {}  # will be map block -> set of variables
        self._mapout = {}
        self._mapdef = {}  # block : defined = killed vars in the block
        self._igraph = None  # interference graph
        super().__init__(function, *args)

    def run(self):
        """Perform all steps related to smart register allocation:

        - Dataflow analysis to compute liveness range of each
          temporary.

        - Interference graph construction

        - Graph coloring

        - Substitution of temporaries by actual locations in the
          3-address code.
        """
        # prints the CFG as a dot file
        if self._debug_graphs:
            self._f.printDot(self._basename + ".dot", view=True)
            print("CFG generated in " + self._basename + ".dot.pdf")
        # TODO (lab5): Move the print&return statements below down as you progress
        # TODO (lab5): in the lab. They must be removed from the final version.
        print("run: stopping here for now")
        return

        # dataflow
        self.set_gen_kill()
        if self._debug:
            self.print_gen_kill()

        self.run_dataflow_analysis()
        if self._debug:
            self.print_map_in_out()

        # conflict graph
        self.build_interference_graph()

        if self._debug_graphs:
            print("printing the conflict graph")
            self._igraph.print_dot(self._basename + "_conflicts.dot")

        # Smart Alloc via graph coloring
        self.smart_alloc(self._basename + "_colored.dot")

        # Finally, modify the code to replace temporaries with
        # regs/memory locations
        self._f.iter_instructions(replace_smart)

    def set_gen_kill(self):
        """Set the _gen and _kill field for each instruction in the function."""
        for ins in self._f.get_instructions():
            if not ins.is_instruction():
                # Labels, comments: no _gen nor _kill
                continue
            for arg in ins.args:
                # Check if the argument is a temporary
                # (isinstance(..., Temporary)), and if so add it to
                # _kill or _gen (use ins.is_read_only() to check
                # whether the first operand is read or written to).
                raise NotImplementedError("Set _gen and _kill for instruction (lab5)")

    def smart_alloc(self, outputname):
        """Allocate all temporaries with graph coloring
        also prints the colored graph if debug.

        Precondition: the interference graph (_igraph) must have been
        initialized.
        """
        if not self._igraph:
            raise MiniCInternalError("hum, the interference graph seems to be empty")
        # Temporary -> Operand (register or offset) dictionary,
        # specifying where a given Temporary should be allocated:
        alloc_dict = {}
        # TODO (lab5): color the graph and get back the coloring (see
        # Libgraphes.py). Then, construct a dictionary Temporary ->
        # Register or Offset. Our version is less than 15 lines
        # including debug log. Be careful, the temporary names in the
        # graph are now strings, and you need to enter Temporary
        # objects in the dictionary. You can get all temporaries in
        # self._f._pool._all_temps, and get the corresponding vertex name
        # using str(temp) to access the associated color.
        # TODO (lab5) : do not forget to update the stacksize at the end!
        self._f._pool.set_temp_allocation(alloc_dict)

    def run_dataflow_analysis(self):
        """Run the dataflow liveness analysis, i.e. compute self._mapin and
        self._mapout based on the ._kill and ._gen fields of individual
        instructions."""
        if self._debug:
            print("Dataflow Analysis")
        countit = 0
        # initialisation of all mapout,mapin sets, and def = kill
        for i in self._f.get_instructions():
            self._mapin[i] = set()
            self._mapout[i] = set()
        stable = False
        while not stable:
            # Iterate until fixpoint :
            # make calls to self._f.dataflow_one_step
            countit = countit + 1
            saveoldout = copy.copy(self._mapout)
            saveoldin = copy.copy(self._mapin)  # structure copy
            self.dataflow_one_step()
            stable = True
            for i in self._f.get_instructions():
                # print("considering node number "+str(i))
                # sets are growing.
                # print (self._mapout[i])
                if (self._mapout[i] > saveoldout[i] or
                        self._mapin[i] > saveoldin[i]):
                    stable = False
        if self._debug:
            print("finished in " + str(countit) + " iterations")
        # print(self._mapin)
        # print(self._mapout)

    def dataflow_one_step(self):
        """Run one iteration of the dataflow analysis. This function is meant
        to be run iteratively until fixpoint."""
        for i in self._f.get_instructions():
            i.dataflow_one_step(self._mapin, self._mapout)

    def interfere(self, t1, t2):
        """Interfere function: True if t1 and t2 are in conflit anywhere in
        the function."""
        raise NotImplementedError("interfere() function (lab5)")

    def build_interference_graph(self):
        """Build the interference graph. Nodes of the graph are temporaries,
        and an edge exists between temporaries iff they are in conflict (i.e.
        iff self.interfere(t1, t2)."""
        for instruction in self._f.get_instructions():
            self._mapdef[instruction] = instruction._kill
        self._igraph = Graph()
        # self._f.printTempList()
        if not self._mapout and not self._mapin:
            raise MiniCInternalError("hum, dataflow sets need to be initialised")

        t = self._f._pool._all_temps
        for v in t:
            # print("add vertex "+str(v))
            self._igraph.add_vertex(str(v))
        tpairs = [(p1, p2) for p1 in t for p2 in t]
        # print(tpairs)
        for (t1, t2) in tpairs:
            if t1 == t2:
                continue  # A temporary cannot conflict with itself
            if self.interfere(t1, t2):
                # print("add edge "+str(t1)+" - "+str(t2))
                self._igraph.add_edge((str(t1), str(t2)))

    def print_gen_kill(self):
        print("Dataflow Analysis, Initialisation")
        i = 0
        for ins in self._f.get_instructions():
            ins.print_gen_kill(i)
            i += 1

    def print_map_in_out(self):  # Prints in/out sets, useful for debug!
        print("In: {" +
              ", ".join(str(x) + ": " + regset_to_string(self._mapin[x])
                        for x in self._mapin.keys()) +
              "}")
        print("Out: {" +
              ", ".join(str(x) + ": " + regset_to_string(self._mapout[x])
                        for x in self._mapout.keys()) +
              "}")
