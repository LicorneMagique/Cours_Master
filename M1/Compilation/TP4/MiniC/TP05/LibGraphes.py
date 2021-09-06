""" A Python Class for Non Oriented Graphs
"""

from copy import deepcopy
# for dot output
from graphviz import Digraph


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class GraphError(Error):
    """Exception raised for self loops
    """

    def __init__(self, message):
        self.message = message


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ edge should be a pair and not (c,c)
        """
        try:
            (vertex1, vertex2) = edge
            if vertex1 == vertex2:
                raise GraphError("no self loop")
            if vertex1 in self.__graph_dict:
                self.__graph_dict[vertex1].append(vertex2)
            else:
                self.__graph_dict[vertex1] = [vertex2]
            if vertex2 in self.__graph_dict:
                self.__graph_dict[vertex2].append(vertex1)
            else:
                self.__graph_dict[vertex2] = [vertex1]
        except GraphError as s:
            print("pb with adding edge: " + s.message)
            pass

    def __generate_edges(self):
        """ A static method generating the set of edges
        (they appear twice in the dictionnary). Returns a list of sets.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def print_dot(self, name="toto", colors={}):
        foo = ['red', 'blue', 'green', 'yellow'] + (['black'] * 10)
        dot = Digraph(comment='Conflict Graph')
        for k in self.__graph_dict:
            if not colors:
                color = "red"  # Graph not colored: red for everyone
            elif k not in colors:
                color = "grey"  # Node not colored: grey
            else:
                color = foo[colors[k]]
            dot.node(k, k, color=color)
        for edge in self.__generate_edges():
            # print edge
            (v1, v2) = list(edge)[0], list(edge)[1]
            dot.edge(v1, v2, dir="none")
        # print(dot.source)
        dot.render(name, view=True)        # print in pdf

    def delete_vertex(self, vertex):  # delete vertex and all the adjacent edges
        gdict = self.__graph_dict
        for neighbour in gdict[vertex]:
            gdict[neighbour].remove(vertex)
        del gdict[vertex]

    def delete_edge(self, edge):
        (v1, v2) = edge
        self.__graph_dict[v1].remove(v2)
        self.__graph_dict[v2].remove(v1)

    def dfs_traversal(self, root):
        seen = []
        todo = [root]
        gdict = self.__graph_dict
        while len(todo) > 0:  # while todo ...
            current = todo.pop()
            seen.append(current)
            for neighbour in gdict[current]:
                if not(neighbour in seen):
                    todo.append(neighbour)
        return seen

    def is_reachable_from(self, v1, v2):
        return v2 in self.dfs_traversal(v1)

    def connex_components(self):
        components = []
        todo = self.vertices()
        done = []
        while todo:
            v = todo.pop()
            if v not in done:
                v_comp = self.dfs_traversal(v)
                components.append(v_comp)
                done.extend(v_comp)
        return components

    def bfs_traversal(self, root):  # list.pop(0) : for dequeuing (on the left...) !
        seen = []
        todo = [root]
        gdict = self.__graph_dict
        while len(todo) > 0:  # while todo ...
            current = todo.pop(0)
            seen.append(current)
            for neighbour in gdict[current]:
                if not(neighbour in seen):
                    todo.append(neighbour)
        return seen

    # see algo of the course
    def color(self, K=None, avoidingnodes=()):
        """color with <= K color (if K is unspecified, use unlimited colors).

        Return 3 values:
        - a map vertex-> color
        - a Boolean, True if the coloring succeedeed
        - The set of nodes actually colored

        Do not color vertices belonging to avoidingnodes.

        Continue even if the algo fails.
        """
        if K is None:
            K = len(self.__graph_dict)
        todo_vertices = []
        is_total = True
        gcopy = deepcopy(self)
        # suppress nodes that are not to be considered.
        for node in avoidingnodes:
            gcopy.delete_vertex(node)
        # append nodes in the list according to their degree and node number:
        while gcopy.__graph_dict:
            todo = list(gcopy.__graph_dict)
            todo.sort(key=lambda v: (len(gcopy.__graph_dict[v]), v))
            lower = todo[0]
            todo_vertices.append(lower)
            gcopy.delete_vertex(lower)
        # Now reverse the list: first elements are those with higher degree
        # print(todo_vertices)
        todo_vertices.reverse()  # in place reversal
        # print(todo_vertices)
        coloring = {}
        colored_nodes = []
        # gdict will be the coloring map to return
        gdict = self.__graph_dict
        for v in todo_vertices:
            seen_neighbours = [x for x in gdict[v] if x in coloring]
            choose_among = [i for i in range(K) if not(
                i in [coloring[v1] for v1 in seen_neighbours])]
            if choose_among:
                # if the node can be colored, I choose the minimal color.
                color = min(choose_among)
                coloring[v] = color
                colored_nodes.append(v)
            else:
                # if I cannot color some node, the coloring is not Total
                # but I continue
                is_total = False
        return (coloring, is_total, colored_nodes)
