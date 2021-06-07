
from DSViz.LinkedListV import LinkedListV


test = LinkedListV(DLL=True, CLL = True)

for i in range(97, 123):
    test.addNode(chr(i))

test.show
