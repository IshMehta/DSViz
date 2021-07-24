from graphviz import Digraph

class TreeV:
    def __init__(self, title = "Tree"):
        self.dot = Digraph(comment= title)
    '''
    delete this part

    #     self.size = 0

    # def addNode(self, parent, left, right):
    #     if self.size == 0:
    #         self.dot.node(parent, parent)
    #     # else:
    #         self.dot.node(left, left)
    #         self.dot.node(right, right)
    #         # self.dot.edges([[str(parent)+str(left), str(parent)+str(right)]])
    #         self.dot.edge(parent, right)
    #         self.dot.edge(parent, left)
    #         self.dot.edge(left, "D")
    '''
            
    def add(self, parent, left = None, right = None):
        self.dot.node(str(parent),str(parent))
        if left is not None:        
            self.dot.edge(str(parent), str(left))
        else:
            self.dot.node(name = str(parent)+'invisl', lable = str(parent)+'invisl', style = 'invis')
            self.dot.edge(str(parent), str(parent)+'invisl')
        if right is not None:
            self.dot.edge(str(parent), str(right))
        else:
            self.dot.node(name = str(parent)+'invisl', lable = str(parent)+'invisl', style = 'invis')
            self.dot.edge(str(parent), str(parent)+'invisl')

    @property
    def show(self):
        self.dot.render('test-output/graph.gv', view=True)
        print(self.dot.source)

