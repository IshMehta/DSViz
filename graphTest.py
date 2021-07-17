from DSViz.GraphV import GraphV
from testC.graph import graph
from DSViz.GraphV import GraphV
adjlist = {'0': ['1','4'],
           '1': ['0','4','3','2'],
           '2': ['1','3'],
           '3': ['1','2','4'],
           '4': ['0','1','3']}
test = graph(adjlist)
test.visuliase('0')

# t = GraphV()
# for e in adjlist.keys():
#     t.add(e, adjlist[e])
# t.show
