# GraphV

`<object> = GraphV(Directed = False)` : Creates an object of this class which will create an undirected graph

!!! info
    `Directed` is set to False by default to create an undirected graph. To create a directed graph set `Directed = True` while object creation.
 

`<object>.add(..parent.. , ..child..)` : creates 2 nodes parent and child while also creating an edge between the two. If `Directed = True` then the edge created will point from parent to child.

!!! warning
    `.add()` method only accpets one parent and one child at a time

For important use-cases check the examples section.

!!! important

To visualise a tree that is not a Binary Tree one can use the directed graph approach.