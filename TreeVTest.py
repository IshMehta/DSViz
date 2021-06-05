from DSViz.TreeV import TreeV

test = TreeV()

test.add("a","b", "c")
test.add("b", left="d")
test.add("d", right="e")
test.show()
