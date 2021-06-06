from DSViz.NoneError import NoneError
from graphviz import Graph
from graphviz import Digraph


class GraphV:

    def __init__(self, Directed=False):

        if not isinstance(Directed, bool):
            if Directed is None:
                raise NoneError('Directed parameter cannot be None')
            raise TypeError("Directed parameter has to be True or False")

        self.dot = Graph(filename='output.gv', engine='sfdp')
        if Directed is True:
            self.dot = Digraph(filename='output.gv', engine='sfdp')
        self.adjList = {}
    
    #TODO: create graph from adjacency list

    def add(self, parent, node):
        
        if parent is None :
            raise NoneError("Parent cannot be None")
        
        if node is None:
            raise NoneError("Child cannot be None")

        if isinstance(parent, (float, int, str)):
            if isinstance(node, (float, int, str)):
                if parent in self.adjList.keys():
                    self.adjList[parent].append(node)
                else:
                    self.adjList[parent] = [node]
            elif isinstance(node, list):
                for element in node:
                    if isinstance(element, (str, float, int)):
                        pass
                    else:
                        raise TypeError('Incorrect data type passed in adjacency list')
            else:
                raise TypeError('Incorrect data type passed as child. Child has to be Integer, String, Float or List of the following.')
        else:
            raise TypeError('Incorrect data type passed as parent. Parent has to be Integer, String or Float.')
    

    
    def show(self):
        
        for parent in self.adjList.keys():
            [self.dot.edge(parent, node) for node in self.adjList[parent]]

        self.dot.render('test-output/graph.gv', view=True)

