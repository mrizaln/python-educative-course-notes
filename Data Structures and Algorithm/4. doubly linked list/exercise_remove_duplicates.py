from doubly_linked_list import *

def remove_duplicates(self):
    cur = self.head
    while cur:
        key = cur.data
        tmp = cur.next
        while tmp:
            if tmp.data == key:
                rem = tmp
                tmp = tmp.next
                self.delete_node(rem)
                continue
            tmp = tmp.next
        cur = cur.next

# other implementation using dictionary (hash table)
def remove_duplicates_dict(self):
    cur = self.head 
    seen = dict()
    while cur:
        if cur.data not in seen:
            seen[cur.data] = 1
            cur = cur.next
        else:
            nxt = cur.next
            self.delete_node(cur)
            cur = nxt

DoublyLinkedList.remove_duplicates = remove_duplicates
DoublyLinkedList.remove_duplicates_dict = remove_duplicates_dict

if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist2 = DoublyLinkedList()
    dllist.prepend(0)
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.prepend(5)
    dllist.add_after_node(3,6)
    dllist.add_before_node(4,9)
    dllist.append(4)
    dllist.append(1)
    dllist.prepend(7)
    dllist.append(6)
    dllist.print_list()
    
    dllist.remove_duplicates()  
    # dllist.remove_duplicates_dict()    
    print("duplicates removed")
    dllist.print_list()

    print()
    for a in range(10): dllist2.append(2)
    dllist2.remove_duplicates()
    dllist2.print_list()