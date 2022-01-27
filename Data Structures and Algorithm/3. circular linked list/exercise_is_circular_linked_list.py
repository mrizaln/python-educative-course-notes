# Determine whether a given linked list is a circular linked list or not

from circular_linked_list import *
from singly_linked_list import *

def is_circular_linked_list(input_list):
    cur = input_list.head
    if cur is None:
        return False
    while cur.next:
        if cur.next == input_list.head:
            return True
        cur = cur.next
    return False

if __name__ == "__main__":
    asdf = CircularLinkedList()
    for a in range(10): asdf.append(a)
    print(is_circular_linked_list(asdf))

    fdasf = CircularLinkedList()
    print(is_circular_linked_list(fdasf))

    dfsa = LinkedList()
    print(is_circular_linked_list(dfsa))

    fdasf.append('a')
    print(is_circular_linked_list(fdasf))
