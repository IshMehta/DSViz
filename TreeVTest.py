from DSViz.TreeV import TreeV

test = TreeV()
test.add("a")
test.add("a","b", "c")
test.add("b", "d")
test.add("d", "e")
test.show()
