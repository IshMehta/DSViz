from DSViz.NoneError import NoneError
from DSViz.ArrayListV import ArrayListV

test =  ArrayListV()



for i in range(50):
    test.addNode(i * 2)

test.show
