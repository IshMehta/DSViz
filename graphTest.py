from DSViz.GraphV import GraphV
from testC.graph import graph
from DSViz.GraphV import GraphV
adjlist = {'0': ['1','4'],
           '1': ['0','4','3','2'],
           '2': ['1','3'],
           '3': ['1','2','4'],
           '4': ['0','1','3']}
test = graph(adjlist)
test.visuliase('4')

adjlist2 = {'A': ['B'], 
            'B': ['C'],
            'C': ['E'],
            'D': ['B'],
            'E': ['D', 'F'],
            'F':[]
            }

# test2 = graph(adjlist2, directed=True)
# test2.visuliase('A')