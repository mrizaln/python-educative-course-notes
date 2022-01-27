class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # print out the entries of linked list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # insertion to the end of list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # insertion to the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert after node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # delete node by value
    def delete_node(self, key):
        cur_node = self.head
        # case if the node to be deleted is head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # delete node by position
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    # determine list length iteratively
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    # determine list length recursively
    def len_recursive(self, node):
        if node is None: return 0
        return 1 + self.len_recursive(node.next)

    # swap two nodes by value
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    # reverse list ireratively
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # reverse list recursively
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if cur is None:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = next
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    # merge two sorted linked list
    # while keeping the final linked list sorted as well
    # assumptiom: each of the sorted linked lists will contain at least one element
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if p is None: return q
        if q is None: return p

        # head condition
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p      # is this line really needed?
                s = p
                p = s.next
            else:
                s.next = q      # is this line really needed/
                s = q
                q = s.next

        if p is None: s.next = q
        if q is None: s.next = p

        self.head = new_head
        return self.head

    # remove duplicates from linked list using (python) hash table
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # remove node
                prev.next = cur.next
                cur = None
            else:
                # have'nt ncountered element before
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next     # probbably is should write this as   cur = cur.next    for readability sake

    # get the Nth-to-last node from a given linked list (node ke-N dari akhir)
    def print_nth_from_last(self, n, method):
        # implemented by decrementing list length until equal to N
        if method == 1:
            total_len = self.len_iterative()
            cur = self.head
            while cur:
                if total_len == n:
                    print(cur.data)
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None: return

        # implemented using two pointer, p and q, q is N nodes ahead of p
        if method == 2:
            p = self.head
            q = self.head

            if n > 0:
                count = 0
                while q:
                    count += 1
                    if count >= n: break
                    q = q.next

                if q is None:
                    print(str(n) + " os greater than the number of nodes in list.")

                while p and q.next:     # should p removed from this conditional? q.next must be encounter None first right?
                    p = p.next
                    q = q.next
                print(p.data)
                return p.data

            else: return None

    # count occurences of data element in a linked list iteratively
    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data: count += 1
            cur = cur.next
        return count

    # count occurences of data element in a linked list recursively
    def count_occurences_recursive(self, node, data):
        if node is None: return 0
        if node.data == data: return 1 + self.count_occurences_recursive(node.next, data)
        else: return self.count_occurences_recursive(node.next, data)

    # rotate linked list
    # rotate using a pivot node, everything following that pivot will be sent to front (it implies a rotation)
    def rotate(self, k):
        # at least the length of list is 2
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    # determine if a linked list is a palindrome
    def is_palindrome_1(self):
        # Solution 1: using a string
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_palindrome_2(self):
        # Solution 2: using a stack
        s = []
        p = self.head

        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_3(self):
        # Solution 3: using two pointer
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1
            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True

        else: return True

    def is_palindrome(self, method):
        if method == 1: return self.is_palindrome_1()
        elif method == 2: return self.is_palindrome_2()
        elif method == 3: return self.is_palindrome_3()



if __name__ == "__main__":

    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.insert_after_node(llist.head.next, "D")
    llist.prepend("Z")

    llist.delete_node("B")
    llist.delete_node("E")
    llist.delete_node("Z")

    for a in list("friend fox"):
        llist.append(a)

    llist.delete_node_at_pos(0)
    llist.delete_node_at_pos(2)
    llist.delete_node_at_pos(4)
    llist.delete_node_at_pos(6)
    llist.delete_node_at_pos(8)

    llist.print_list()

    print("the length of the list (counted iteratively): ", llist.len_iterative())
    print("the length of the list (counter recursively): ", llist.len_recursive(llist.head))

    llist.swap_nodes("r", "C")
    print("Swapping nodes r and C that are not head nodes")
    llist.print_list()

    llist.swap_nodes("D", "C")
    print("Swapping nodes D and C where key_1 is head node")
    llist.print_list()

    llist.swap_nodes("f", "D")
    print("Swapping nodes f and D")
    llist.print_list()

    llist.swap_nodes("o", "d")
    print("Swapping nodes o and d")
    llist.print_list()

    llist.swap_nodes("s", "x")
    print("Swapping nodes s and x where both keys not exist")
    llist.print_list()

    print("reverse iteratively!")
    llist.reverse_iterative()
    llist.print_list()

    print("reverse recursively!")
    llist.reverse_iterative()
    llist.print_list()

    print("\n\n\n\n")

    llist_1 = LinkedList()
    llist_2 = LinkedList()

    llist_1.append(1)
    llist_1.append(5)
    llist_1.append(7)
    llist_1.append(9)
    llist_1.append(10)

    print("linked list 1:")
    llist_1.print_list()

    llist_2.append(2)
    llist_2.append(3)
    llist_2.append(4)
    llist_2.append(6)
    llist_2.append(8)

    print("linked list 2:")
    llist_2.print_list()

    llist_1.merge_sorted(llist_2)

    print("merged list")
    llist_1.print_list()

    print("\n\n\n\n")

    llist = LinkedList()
    llist.append(1)
    llist.append(6)
    llist.append(1)
    llist.append(4)
    llist.append(2)
    llist.append(2)
    llist.append(4)

    print("Original Linked List")
    llist.print_list()
    print("Linked List After Removing Duplicates")
    llist.remove_duplicates()
    llist.print_list()

    print("\n\nprint node ke_N ti akhir")

    print(llist.print_nth_from_last(4,1))
    print(llist.print_nth_from_last(4,2))

    print("\n\n\nsome linked list with elements:")
    llist_2 = LinkedList()
    llist_2.append(1)
    llist_2.append(2)
    llist_2.append(1)
    llist_2.append(3)
    llist_2.append(1)
    llist_2.append(4)
    llist_2.append(1)
    llist_2.print_list()
    print("count occurences of data: 1")
    print(llist_2.count_occurences_iterative(1))
    print(llist_2.count_occurences_recursive(llist_2.head, 1))

    print("rotate by pivot: 4th node")
    llist_2.rotate(4)
    llist_2.print_list()

    print("\n\nis palindrome?")
    llist = LinkedList()
    for c in "heheh": llist.append(c)
    llist.print_list()
    print(llist.is_palindrome(1), "\n")

    llist.append(c)
    llist.print_list()
    print(llist.is_palindrome(2))
