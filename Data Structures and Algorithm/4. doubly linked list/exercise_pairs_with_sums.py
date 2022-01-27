# Create a function that return list of pair from a doubly linked list which sum to certain number

from doubly_linked_list import *
from exercise_remove_duplicates import *

def pairs_with_sum(self, sum_val):    
    pair_1 = self.head
    pairs = []
    while pair_1:
        key_1 = pair_1.data
        pair_2 = pair_1.next
        while pair_2:
            key_2 = pair_2.data
            if key_1 + key_2 == sum_val:
                pairs.append("({},{})".format(key_1, key_2))
            pair_2 = pair_2.next
        pair_1 = pair_1.next
    return pairs

DoublyLinkedList.pairs_with_sum = pairs_with_sum

if __name__ == "__main__":
    dllist = DoublyLinkedList()
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

    print("pairs with sum to 6: ",dllist.pairs_with_sum(6))