
from DSViz.GraphV import GraphV

class directedGraph:

    def __init__(self, adjlist, directed = False):
        self.adjlist = adjlist
        self.viz = GraphV(Directed=directed)
        
    def show(self):
        for node in self.adjlist:
            for element in self.adjlist[node]:
                self.viz.add(node, element)
        self.viz.show


    
