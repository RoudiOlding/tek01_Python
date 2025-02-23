## 1. ARRAYS
import array as arr

a = arr.array('d', [1.1, 3.5, 4.5]) # Creating an array
print(a)
print(a[0]) # Accessing elements

# append
a.append(5.4)
print(a)

# concatenate
b = arr.array('d', [2.0, 3.0, 4.0])
a += b
print(a)

# removing
a.pop(2)
print(a)

# slicing
print(a[0:2])

## 2. LINKED LISTS

# Using colelctions module
from collections import deque
llist = deque([1, 2, 3])
print(llist)

# append
llist.append(4)
print(llist)

# appendleft
llist.appendleft(0)
print(llist)

# pop
llist.pop()
print(llist)

# queue
from collections import deque
queue = deque()
queue

queue.append('Mary')
queue.append('John')
queue.append('Susan')

# Simulate the attendace of each one
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

# Implementing a linked list (manually)
class LinkeList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
    def __iter__(self): # Allows to iterate over the linked list, wihout this method, it would raise an error
        node = self.head
        while node is not None:
            yield node # Yield is a generator, it will return the value and pause the execution of the function. Like print, but if you use print, it will print the memory address of the object
            node = node.next

    # Implementing add new node
    def add_first(self, node): # basically, it will add a new node to the beginning of the linked list
        node.next = self.head
        self.head = node

    # Implementing add new node to the end
    def add_last(self, node):
        if self.head is None: # If the linked list is empty, the new node will be the head
            self.head = self.node
            return
        for current_node in self: # If the linked list is not empty, it will iterate over the linked list until it finds the last node
            pass
        current_node.next = node # Assign the new node to the next attribute of the last node

    # Implementing add new node after a specific node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception('Node with data %s not found' % target_node_data)
    
    # Implementing add new node before a specific node
    def add_before(self, target_node_data, new_node):
        if self.head is None: # If the linked list is empty, it will raise an exception
            raise Exception('List is empty')
        if self.head.data == target_node_data: # If the linked list is not empty, but the target node is the head, it will add the new node to the beginning of the linked list
            return self.add_first(new_node) # It will call the add_first method
        prev_node = self.head # If the linked list is not empty and the target node is not the head, it will iterate over the linked list until it finds the target node
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node # When it finds the target node, it will assign the new node to the next attribute of the previous node
                new_node.next = node # And the target node to the next attribute of the new node
                return # It will return the new node
            prev_node = node # If the target node is not found, it will assign the current node to the previous node
        raise Exception('Node with data %s not found' % target_node_data)
    
    # Implementing remove a node
    def remove_node(self, target_node_data):
        if self.head is None: # If the linked list is empty, it will raise an exception
            raise Exception('List is empty')
        if self.head.data == target_node_data: # If the linked list is not empty and the target node is the head, it will remove the head
            self.head = self.head.next
            return
        prev_node = self.head # If the linked list is not empty and the target node is not the head, it will iterate over the linked list until it finds the target node
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next # When it finds the target node, it will assign the next attribute of the previous node to the next attribute of the target node
                return
            prev_node = node
        raise Exception('Node with data %s not found' % target_node_data)
    
    def get_specific_position(self, target_position):
        if self.head is None: # Linked list empty
            raise Exception('List is empty')
        
        if target_position == 1: # Linked list with one element
            return self.head.data
        
        current_position = 1
        for node in self:
            if current_position == target_position:
                return node.data
            current_position += 1
        raise Exception('Position %s not found' % target_position)
    
        
    # Implementing reverse linked list
    def reverse_linked_list(self):
        prev_node = None # It will store the previous node
        current_node = self.head # It will store the current node
        while current_node is not None: # It will iterate over the linked list
            next_node = current_node.next # It will store the next node
            current_node.next = prev_node # It will assign the previous node to the next attribute of the current node
            prev_node = current_node # It will assign the current node to the previous node
            current_node = next_node # It will assign the next node to the current node
        self.head = prev_node # It will assign the previous node to the head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    
llist = LinkeList()
first_node = Node('a')
llist.head = first_node
print(llist)
second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)

for value in llist:
    print(value)

# Adding a new node (start)
new_node = Node('d')
llist.add_first(new_node)
print(llist)

# Adding a new node (end)
new_node2 = Node ('e')
llist.add_last(new_node2)
print(llist)

# Adding a new node after a specific node
new_node3 = Node('f')
llist.add_after('b', new_node3)
print(llist)

# Adding a new node before a specific node
new_node4 = Node('g')
llist.add_before('c', new_node4)
print(llist)

# Removing a node
llist.remove_node('b')
print(llist)

# Reversing the linked list
llist.reverse_linked_list()
print(llist)