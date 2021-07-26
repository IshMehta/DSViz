
from DSViz.GraphV import GraphV

class graph:

    def __init__(self, adjlist, directed = False):
        self.adjlist = adjlist
        self.viz = GraphV(Directed=directed)
        self.source = None
        

    def visualise(self, start):
        
        edgeSet = set()
        VS = set()
        stack = []
        
        curr = start
        stack.append(curr)
        while len(stack) != 0:
            curr = stack.pop(-1)
            VS.add(curr)
            for adjacent in self.adjlist[curr]:
                found = False
                for element in edgeSet:
                    if curr in element and adjacent in element:
                        found = True
                if not found:
                    self.viz.add(curr, adjacent)
                if adjacent not in VS:
                    stack.append(adjacent)
                edgeSet.add((adjacent, curr))
        
        self.viz.show
    
