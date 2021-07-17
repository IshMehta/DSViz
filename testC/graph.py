import sys
sys.path.append('..')
from DSViz.GraphV import GraphV

class graph:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = {}
        
    def __init__(self, adjlist):
        self.adjlist = adjlist

    def visuliase(self, start):
        viz = GraphV()
        edgeSet = set()
        VS = set()
        stack = []
        
        curr = start
        # print(self.adjlist[curr])
        
        stack.append(curr)
        
        while len(stack) != 0:
            # print(stack)
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
        