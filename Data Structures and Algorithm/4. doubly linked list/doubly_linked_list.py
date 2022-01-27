# Doubly linked list is very similar to the singly linked list except for the difference of the previous pointer.
#  In a doubly linked list, a node is made up of the following components:
    # Data
    # Next (Points to the next node)
    # Prev (Points to the previous node)

from dataclasses import dataclass
from tokenize import Double


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    # insert node after a certain node with data: key
    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
                return
            cur = cur.next

    # insert node before a certain node with data: key
    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                return
            cur = cur.next

    # delete node
    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next

    # delete node by key
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # case 1: delete the only node present
                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                
                # case 2: delete head node
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # case 3: delete non-head node but not tail
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # case 4: delete tail
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next

    # reverse the list
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            prev = cur.prev
            cur.prev = cur.next
            cur.next = prev
            cur = cur.prev
        if prev:
            self.head = prev.prev

    # print reversed list without reversing it
    def print_reverse_list(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        
        while cur:
            print(cur.data)
            cur = cur.prev

if __name__ == "__main__":
    dllist = DoublyLinkedList()
    # dllist2 = DoublyLinkedList()
    dllist.prepend(0)
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.prepend(5)
    dllist.add_after_node(3,6)
    dllist.add_before_node(4,9)

    dllist.delete(1)
    dllist.delete(7)
    dllist.delete(5)
    dllist.delete(4)
    
    dllist.print_list()

    # dllist2.append(1)
    # dllist2.print_list()
    # dllist2.delete(1)
    # dllist2.print_list()
    
    dllist.reverse()
    dllist.print_list()
