# Class LinkedListV

`<object> = LinkedListV(DLL = False, CLL = False)` : Creates an object of LinkedListV class

!!! info
    We provide some flexibility while creating an object of this class. By default DLL and CLL are set to False.

    * DLL stands for 'Doubly Linked List'
    * CLL stands for 'Circular Linked List'

    While object creation, DLL and CLL can be set to True or False and accordingly the appropriate linked list will be rendered.

`<object>.addNode(..item..)` will add node to the linked list beginning from head to tail.

!!! note
    You can only add one item at a time. We suggest you iterate over the linked List and call the `.addNode()` method on every item.

 `<object>.show` : Once every node has been added, use this property to render the linked list.