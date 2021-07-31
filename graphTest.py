
# from testC.graph import graph
from testC.directedGraph import graph

adjlist = {'0': ['1','4'],
           '1': ['0','4','3','2'],
           '2': ['1','3'],
           '3': ['1','2','4'],
           '4': ['0','1','3']}

# adjlist = {'A': ['B'], 
#             'B': ['C'],
#             'C': ['E'],
#             'D': ['B'],
#             'E': ['D', 'F'],
#             'F':[]
#             }
# test = graph(adjlist)
# test.visualise('1')


# with open ('DSViz/test-output/graph.gv') as f:
#     # lines = f.read().rstrip()
#     result = f.readlines()
# print(result)
# if result == ['graph {\n', '\t4 -- 0\n', '\t4 -- 1\n', '\t4 -- 3\n', '\t3 -- 1\n', '\t3 -- 2\n', '\t2 -- 1\n', '\t1 -- 0\n', '}\n']:
#     print("True")
# else:
#     print('False')
# adjlist2 = {'A': ['B'], 
#             'B': ['C'],
#             'C': ['E'],
#             'D': ['B'],
#             'E': ['D', 'F'],
#             'F':[]
#             }

# test2 = graph(adjlist2, directed=True)
# test2.visuliase('A')

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

test3 = graph(adjlist3, directed=True)
test3.show()