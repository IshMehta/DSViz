# TreeV

`<object> = TreeV()` : Creates an object for this class

There are 4 variations of the add method to add nodes to the tree:

* `<object>.add(..parent..)` : creates a single node with value = parent with children set to None/null
* `<object>.add(..parent.., left = ..child..)` : creates a parent node with a single left child
* `<object>.add(..parent.., right = ..child..)` : creates a parent node with a single right child
* `<object>.add(..parent.., left = child, right = ..child..)` : creates a parent node with a single left child and single right child

!!! warning
    Two nodes with the same value cannot be created as each node is recognised by its value. While this may be a problem, it makes editing the tree relatively easier as one can add a node just by referenceing the parent nodes value.

`<object>.show` : Once every node has been added, use this property to render the tree.