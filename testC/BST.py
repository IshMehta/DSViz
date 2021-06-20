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
        if self.root is None:
            self.root = node



    
