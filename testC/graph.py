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
        VS = set()
        stack = []
        
        curr = start
        # print(self.adjlist[curr])
        VS.add(curr)
        stack.append(curr)
        
        while len(stack) != 0:
            for adjacent in self.adjlist[curr]:
                # if adjacent not in VS:
                    # VS.add(adjacent)
                stack.append(adjacent)
                viz.add(curr, adjacent)
            curr = stack[-1]
            stack.pop(len(stack) - 1)

        viz.show
        