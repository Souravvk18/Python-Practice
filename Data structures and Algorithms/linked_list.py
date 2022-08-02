class Node:
    '''
    An object for storing a single node of a linked list.
    models two attributes - data and link to the next node in the list
    '''
    data=None
    next_node=None

    def __init__(self, data):
        self.data=data
    
    def __repr__(self):
        return "Node data:%s" % self.data

class LinkedList:

    """
    single Linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        returns the number of nodes in the list
        Takes O(n) time
        """
        current= self.head
        count=0

        while current:
            count += 1
            current= current.next_node

        return count

    def add(self, data):

        """
        Add new node containing data at head of the list
        takes O(1) time. 
        """
        new_node = Node(data)
        new_node.next_node= self.head
        self.head = new_node



    def search(self, key):
        """
        search for the first node containing data that matches the key
        return the node or None if not found.
        """
        current = self.head

        while current:
            if current.data ==key:
                return current
            else:
                current=current.next_node
        return None


    def insert(self, data, index):
        """
            inserts a new node containing data at index position
            insertion takes O(1) time but finding 
            the node at the insertion point takes O(n) time. 
        """
        if index== 0:
            self.add(data)

        if index> 0:
            new= Node(data)

            position = index
            current = self.head

            while position > 1:
                current = new.next_node
                position -= 1

            prev_node= current
            next_node= current.next_node

            prev_node.next_node= new
            new.next_node= next_node
           
    def remove(self, key):
        """
        removes node containing data that matches the key returns 
        the node or None if key doesnot exist takes O(n) time.
        """
        current= self.head
        previous= None
        found = False

        while current and not found:
            if current.data ==key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data ==key:
                found = True
                previous.next_node= current.next_node
            else:
                previous= current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index ==0:
            return self.head
        else:
            current= self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

    def __repr__(self):

        '''
        return a string representation of the list
        take O(n) time
        '''
    
        nodes = []
        current= self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)

"""
o/p- 
PS C:\VS code\Data structures and Algorithms> python -i linked_list.py
>>> l=LinkedList()
>>> l.add(10)
>>> l.size()
1
>>> l.add(20)
>>> l.add(30)
>>> l.add(40)
>>> l.size()
4
>>> l
<__main__.LinkedList object at 0x000001CEFAD90AF0>
>>> exit()
PS C:\VS code\Data structures and Algorithms> python -i linked_list.py
>>> l= LinkedList()
>>> l.add(1)
>>> l.add(2)
>>> l.add(3)
>>> l
[Head: 3]-> [2]-> [Tail: 1]
>>> l.add(10)
>>> l.add(30)
>>> l.add(40)
>>> l
[Head: 40]-> [30]-> [20]-> [10]-> [3]-> [2]-> [Tail: 1]
>>> n=l.search(20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'LinkedList' object has no attribute 'search'
>>> ^Z

PS C:\VS code\Data structures and Algorithms> python -i linked_list.py
>>> l= LinkedList()
>>> l.add(5)
>>> l.add(10)
>>> l.add(15)
>>> l.size()
3
>>> n= l.search(10)
>>> m
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'm' is not defined
>>> n
Node data:10
>>> l
[Head: 15]-> [10]-> [Tail: 5]
>>> l.add(20)
>>> l.add(25)
>>> l
[Head: 25]-> [20]-> [15]-> [10]-> [Tail: 5]
>>> ^Z

>>> l= LinkedList()
>>> l

>>> l.add(10)
>>> l.add(20)
>>> l.add(30)
>>> l

>>> l.remove(10)
Node data:10
>>> l
[Head: 30]-> [Tail: 20]
"""








