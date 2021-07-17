


class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

        

    def __init__(self):
        self.root = None
        
    def add(self, value):
        node = self.Node(value)
        curr = self.root

        while curr is not None or curr == value:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right

        if curr is None:
            self.root = node
        
    def preorder(self, curr):
        self.preorder(curr.left)
        self.preorder(curr.right)
        self.preorder(curr)
        
            

    # def addHelper(self, curr, value):

        
            



    
