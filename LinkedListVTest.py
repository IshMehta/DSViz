
from DSViz.LinkedListV import LinkedListV


test = LinkedListV(CLL=True, DLL=True)

for i in range(97, 123):
    test.list.append(chr(i))
    print(chr(i))
test.show
