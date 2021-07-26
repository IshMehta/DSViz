

from DSViz.TreeV import TreeV

class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

        

    def __init__(self):
        self.root = None
        self.viz = TreeV()
         
        
    def postorderVisualiser(self, curr):
        if curr is None:
            return
        else:
            if curr.left is None and curr.right is None:
                self.viz.add(curr.value)
            else:
                if curr.left is None:
                    self.viz.add(curr.value, right= curr.right.value)
                elif curr.right is None:
                    self.viz.add(curr.value, left= curr.left.value)
                else:    
                    self.viz.add(curr.value, curr.left.value, curr.right.value)
                self.postorderVisualiser(curr.left)
                self.postorderVisualiser(curr.right)
            
    def renderTree(self):
        self.viz.show
            
    def add(self, value):
        self.root = self.addHelper(self.root, value)

    def addHelper(self, curr, value):
        if curr is None:
            return self.Node(value)
        elif value < curr.value:
            curr.left = self.addHelper(curr.left, value)
        elif value > curr.value:
            curr.right = self.addHelper(curr.right, value)
        return curr

        
            



    
