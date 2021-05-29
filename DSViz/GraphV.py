from graphviz import Graph
from graphviz import Digraph

class GraphV:
    def __init__(self, Directed=False):
        self.dot = Graph(filename='output.gv', engine='sfdp')
        if Directed is True:
            self.dot = Digraph(filename='output.gv', engine='sfdp')
    
    #TODO: create graph from adjacency list

    def add(self, parent, node):
        self.dot.edge(parent, node)


    def show(self):
        self.dot.view()
        # self.dot.render('test-output/graph.gv', view=True)