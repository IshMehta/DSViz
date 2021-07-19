import sys
sys.path.append('..')
from DSViz.GraphV import GraphV

class graph:

    def __init__(self, adjlist, directed = False):
        self.adjlist = adjlist
        self.directed = directed

    def visuliase(self, start):
        viz = GraphV(Directed=self.directed)
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
                    viz.add(curr, adjacent)
                if adjacent not in VS:
                    stack.append(adjacent)
                edgeSet.add((adjacent, curr))
                print(edgeSet)
            

        viz.show
        