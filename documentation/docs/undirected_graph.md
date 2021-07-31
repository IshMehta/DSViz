# Undirected Graph Example

```python
from DSViz import GraphV

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



        viz.show
```

One can then utilise this 'visualise' method created.

```python
adjlist = {'0': ['1','4'],
           '1': ['0','4','3','2'],
           '2': ['1','3'],
           '3': ['1','2','4'],
           '4': ['0','1','3']}
test = graph(adjlist)
test.visuliase('4')
```


<img src ="https://github.com/IshMehta/DataStructureViz/blob/main/resources/GraphExample.jpg?raw=true" width="350"/>

A similar approach can be followed to visualise any form of graph regardless of its implementation specifics.
