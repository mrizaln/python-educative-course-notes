# The first number that we append to the linked list represents the unit place and will be the 
# least significant digit of a number. The next numbers appended to the linked list will subsequently 
# represent the tenth, hundredth, thousandth, and so on places.
    
    # example: a linked list    3 -> 2 -> 4 -> 5    represent a number 5423

from singly_linked_list import *

def sum_two_lists(self, llist):
    p = self.head  
    q = llist.head

    sum_llist = LinkedList()

    carry = 0
    while p or q:
        if not p:
            i = 0
        else:
            i = p.data
        if not q:
            j = 0 
        else:
            j = q.data
        s = i + j + carry
        if s >= 10:
            carry = 1
            remainder = s % 10
            sum_llist.append(remainder)
        else:
            carry = 0
            sum_llist.append(s)

        # uncomment these commented statement below to turn the method to directly use list_1 as its sum with list_2
        # in other word: list_1 = list_1 + list_2
        #if p:
        #    p.data = remainder
        #else:
        #    self.append(remainder)

        if p:
            p = p.next
        if q:
            q = q.next

    return sum_llist


LinkedList.sum_two_lists = sum_two_lists

if __name__ == "__main__":
    list_1 = LinkedList()
    list_2 = LinkedList()
    for i in "234758736745865567885745678"[::-1]: 
        list_1.append(int(i))
    for j in "354677543546786546786547865"[::-1]:
        list_2.append(int(j))


    list_1.print_list()
    print()
    list_2.print_list()
    print()
    list_1 = list_1.sum_two_lists(list_2)
    list_1.print_list()