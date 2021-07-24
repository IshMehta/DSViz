from DSViz.GraphV import GraphV
from testC.BST import BST
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
