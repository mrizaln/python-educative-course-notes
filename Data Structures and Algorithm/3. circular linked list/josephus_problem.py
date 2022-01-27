# https://en.wikipedia.org/wiki/Josephus_problem

# Children often play a counting-out game to randomly select one person from the group by
# singing a rhyme. The purpose is to select one person, either as a straightforward
# winner or as someone who is eliminated.

# Josephus problem is related to this concept. In this problem, people are standing in
# one circle waiting to be executed. Following points list the specifications of Josephus
# problem:

#     The counting out begins at a specified point in a circle and continues around the
#     circle in a fixed direction.
#
#     In each step, a certain number of people are skipped and the next person is executed

# For example, if we have n people, and k−1 people are skipped every time, it means that
# the kth person is executed. Here, k is the step-size.

from circular_linked_list import *

def josephus_circle(self, step):
    cur = self.head

    length = len(self)
    while length > 1:
        count = 1
        while count != step:
            cur = cur.next
            count += 1
        print("KILL: " + str(cur.data))
        self.remove_node(cur)
        cur = cur.next
        length -= 1

CircularLinkedList.josephus_circle = josephus_circle

if __name__ == "__main__":
    cllist = CircularLinkedList()
    for i in range(1,101): cllist.append(i)

    cllist.josephus_circle(int(input("input step (integer): ")))
    cllist.print_list()
