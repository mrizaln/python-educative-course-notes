# The first number that we append to the linked list represents the unit place and will be the 
# least significant digit of a number. The next numbers appended to the linked list will subsequently 
# represent the tenth, hundredth, thousandth, and so on places.
    
    # example: a linked list    3 -> 2 -> 4 -> 5    represent a number 5423

from singly_linked_list import *

def sum_two_lists(self, llist):
    list_1 = self.head
    list_2 = llist.head
    prev = None
    carry = 0

    while list_1 and list_2:
        sum = list_1.data + list_2.data + carry
        if sum >= 10: 
            carry = 1
            sum -= 10
        else:
            carry = 0
        list_1.data = sum
        prev = list_1
        list_1 = list_1.next
        list_2 = list_2.next

    if list_1 == None and list_2 == None:
        pass
    else:
        list_1 = prev
        if list_2: 
            list_1.next = list_2
            list_1 = list_1.next

        while list_1:
            sum = list_1.data + carry
            if sum >= 10:
                carry = 1
                sum -= 10
            else:
                carry = 0
            list_1.data = sum
            prev = list_1
            list_1 = list_1.next
    
    if carry: self.append(carry)

    return self

# this implementation is direct, no return statement required, so no assignment required, 
# the sum is assigned into the object that called this function
# if list_1 called this function, then
#    list_1 = list_1 + list_2

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