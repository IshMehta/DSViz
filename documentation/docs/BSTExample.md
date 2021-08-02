# Binary Search Tree Example

The following is an example on a BST class which uses the TreeV class form the DSViz package to visualise the tree that will be created.

```python
from DSViz import BinaryTreeV

class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

        

    def __init__(self):
        self.root = None
        self.viz = BinaryTreeV()
         
        
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
```
One can make simple changes to a tree traversal. in this example we have used the postorder traversal as seen in the postorderVisualiser() method. Using this is quite simple.

```python
test = BST()
test.add(100)
test.add(50)
test.add(25)
test.add(27)
test.add(51)
test.add(55)
test.add(155)
test.postorderVisualiser(test.root)
test.renderTree()
```

This results in the following render.

<img src='https://github.com/IshMehta/DSViz/blob/main/resources/TreeExample2.PNG?raw=true' width='650'>
