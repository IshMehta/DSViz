
from DSViz.NoneError import NoneError
from graphviz import Graph
from graphviz import Digraph


class GraphV:

    def __init__(self, Directed=False):

        if not isinstance(Directed, bool):
            if Directed is None:
                raise NoneError('Directed parameter cannot be None')
            raise TypeError("Directed parameter has to be True or False")

        # self.dot = Graph(filename='output.gv', engine='sfdp')
        # TODO: ISSUE - sfdp engine does not work on windows
        self.dot = Graph(filename='output.gv')
        if Directed is True:
            # self.dot = Digraph(filename='output.gv', engine='sfdp')
            self.dot = Digraph(filename='output.gv')
        self.adjList = {}
    
    #TODO: should we seperate the adding by individual node and adding by list into 2 diff methods ?

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

    # TODO: ISSUE- adj list implementation, creates double lines, shouldn't do that. OR remove adjlist implementation
    
    
            elif isinstance(node, list):
                # if parent exists, add
                if parent not in self.adjList.keys():
                    self.adjList[parent] = []

                for element in node:
                    if isinstance(element, (str, float, int)):
                        self.adjList[parent].append(element)
                    else:
                        raise TypeError('Incorrect data type passed in adjacency list')
                '''

                delete this part

                # else:

                #     for element in node:
                #         if not isinstance(element, (str, float, int)):
                #             raise TypeError('Incorrect data type passed in adjacency list')
                #     self.adjList[parent] = [node]
                '''
            else:
                raise TypeError('Incorrect data type passed as child. Child has to be Integer, String, Float or List of the following.')
        else:
            raise TypeError('Incorrect data type passed as parent. Parent has to be Integer, String or Float.')
    

    @property
    def show(self):
        # print(self.adjList)
        for parent in self.adjList.keys():
            
            [self.dot.edge(parent, node) for node in self.adjList[parent]]
        print(self.dot.source)
        self.dot.render('test-output/graph.gv', view=True)

