from graphviz import Digraph
from DSViz.NoneError import NoneError

class TreeV:
    def __init__(self):
        self.dot() = Digraph

    def addTree(self, parent ,adjacentNodesList):
        if parent is None:
            raise NoneError("Parent node cannot be None")
        if adjacentNodesList is None:
            self.dot.node(str(parent), str(parent))
        if not isinstance(adjacentNodesList, list):
            raise TypeError("Adjacent nodes have to be a list")
        for node in adjacentNodesList:
            if node is None:
                raise NoneError("Child node in tree cannot be None")
            if not isinstance(node,(str, float, int)):
                raise TypeError("Child node in tree has to be String, Integer or Float")
            self.dot.edge(str(node), str(node))

    @property
    def show(self):
        self.dot.render('DSViz/test-output/graph.gv', view=True)