# Getting Started


DSViz is a simple and intuitive Python interface to multiple packages in order to help visualise different data structres while codng them. This package is developed mainly for students or developers who are in the process of learning data structures. 

</br>  

How to use it ? Simple ! 

Step 1. Iterate over your Data Structure using the appropriate class

Step 2. Call the .add() method on each node

Step 3. Once you have added every node, use the .show property 

Step 4. Keep Coding ;)

Here are a few examples...

## Array List

Goal: Array List which stores even numbers from 2-100

``` python 
from DSViz import ArrayListV
test =  ArrayListV()

for i in range(1,51):
    test.addNode(i * 2)

test.show
```
![Array List Example](https://github.com/IshMehta/DSViz/blob/main/resources/ArrayListExample.gif?raw=true)

## Linked List

Goal: Circular Doubly Linked List which stores alphabets from a-z

> addNode(node) : adds nodes to the back of a linked list

We suggest you start at the head of the linked list and iterate to the end and call the add method on each node. The below example gives an idea on how the add method works and how the data structure is visualised.
> LinkedListV object upon creation has default CLL = False and DLL = False. These can be toggled upon object creation to change the how the pointers in the visualisation.

```python
from DSViz import LinkedListV
test = LinkedListV(CLL=True, DLL=True)

for i in range(97, 123):
    test.addNode(chr(i))
    
test.show
```
![Linked List Example](https://github.com/IshMehta/DSViz/blob/main/resources/LinkedListExample.gif?raw=true)

## Binary Tree

Goal: Visualise a tree

```python
from DSViz import BinaryTreeV
test = BinaryTreeV()

test.add("a","b","c")
test.add("b", left="d")
test.add("d", right="e")
test.show()
```

<img src='https://github.com/IshMehta/DSViz/blob/main/resources/TreeExample.png?raw=true' width='500'/>


## Graph

Goal: Visualise an undirected graph

>add(node1, node2) : creates an edge between two nodes, if the node exists, it creates an edge between the two, if node does not exist, it creates the node and the edge.

We suggest you to use the add method while iterating over your graph using BFS or DFS as per your choice. The below example is just a simple explanation of how the add method works.

```python
from DSViz import GraphV
test = GraphV()

test.add('run', 'intr')
test.add('intr', 'runbl')
test.add('runbl', 'run')
test.add('run', 'kernel')
test.add('kernel', 'zombie')
test.add('kernel', 'sleep')
test.add('kernel', 'runmem')
test.add('sleep', 'swap')
test.add('swap', 'runswap')
test.add('runswap', 'new')
test.add('runswap', 'runmem')
test.add('new', 'runmem')
test.add('sleep', 'runmem')

test.show
```

![Graph Example](https://github.com/IshMehta/DSViz/blob/main/resources/GraphExample.png?raw=trueg)










                
            




 
