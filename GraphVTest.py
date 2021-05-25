from DSViz.GraphV import GraphV

test = GraphV()
test.add("a")
test.add("a","b", "c")
test.add("b", "d")
test.add("d", "e")
test.show()
