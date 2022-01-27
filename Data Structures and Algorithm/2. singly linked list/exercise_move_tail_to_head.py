from shutil import move
from singly_linked_list import *

def move_tail_to_head(self):
    if self.head and self.head.next:
        curr = self.head
        prev = None

        while curr.next:
            prev = curr
            curr = curr.next

        curr.next = self.head
        self.head = curr
        prev.next = None

# adding new method into existing class in single_linked_list (not recommended)
LinkedList.move_tail_to_head = move_tail_to_head

if __name__ == "__main__":
    llist = LinkedList()

    for a in "quick": llist.append(a)

    print("before moving tail to head:")
    llist.print_list()
    
    llist.move_tail_to_head()
    print("after moving tail to head:")
    llist.print_list()

