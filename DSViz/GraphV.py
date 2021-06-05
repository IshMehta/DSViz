from graphviz import Graph
from graphviz import Digraph

import os

class GraphV:
    def __init__(self, Directed=False):
        self.dot = Graph(filename='output.gv', engine='sfdp')
        if Directed is True:
            self.dot = Digraph(filename='output.gv', engine='sfdp')
        self.adjList = {}
    
    #TODO: create graph from adjacency list

    def add(self, parent, node):
        # if parent in self.adjList.keys():
        #     self.adjList[parent].append(node)
        # else:
        #     self.adjList[parent] = [node]
        self.dot.edge(parent, node)

    
    def show(self):
        

        # for parent in self.adjList.keys():
        #     [self.dot.edge(parent, node) for node in self.adjList[parent]]

        self.dot.render('test-output/graph.gv', view=True)

        # # cleanup folder
        # os.remove('test-output/graph.gv')
        # os.remove('test-output/graph.gv.pdf')
        # os.rmdir('test-output')