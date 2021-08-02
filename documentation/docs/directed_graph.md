# Directed Graph Example

``` python
from DSViz import GraphV

class directedGraph:

    def __init__(self, adjlist, directed = False):
        self.adjlist = adjlist
        self.viz = GraphV(Directed=directed)
        
    def show(self):
        for node in self.adjlist:
            for element in self.adjlist[node]:
                self.viz.add(node, element)
        self.viz.show
```

One can then utilise this 'show' method created.

``` python
adjlist3 = {
 1 : [6,4],  
 2: [9,7,5],
 3: [5,8],
 4: [9],
 5: [13],
 6: [10,9],
 7: [11,12,13],
 8: [14],
 9: [15],
 10: [],
 11: [15],
 12: [],
 13: [],
 14:[],
 15:[]
}

test = directedGraph(adjlist3, directed=True)
test.show()
```

<img src ="https://github.com/IshMehta/DataStructureViz/blob/main/resources/directedGraphExample.PNG?raw=true" width="700"/>

A similar approach can be followed to visualise any form of graph regardless of its implementation specifics.