# Circular linked list is very similar to a singly linked list except for the fact that the next of the tail node is
# the head node instead of null.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    # remove node by key
    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next
    # remove node
    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    # calculate circular linked list length
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head: break
        return count

    # split linked list into two halves
    def split_list(self):
        size = len(self)

        if size == 0: return None
        if size == 1: return self.head

        mid = size // 2
        count = 0

        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print()
        split_cllist.print_list()



if __name__ == "__main__":
    cllist = CircularLinkedList()
    cllist.append("C")
    cllist.append("D")
    cllist.prepend("B")
    cllist.prepend("A")
    cllist.print_list()
    print()
    cllist.remove("A")
    cllist.remove("C")
    cllist.print_list()

    print(cllist.__len__())
    cllist.append("F")
    cllist.append("G")
    cllist.append("H")
    cllist.append("I")
    print()
    cllist.split_list()
