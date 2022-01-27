from binary_tree import *
from level_order_traversal import Queue
from the_stack import Stack

def __len__(self):
    return self.size()

def size(self):
    return len(self.items)

def __str__(self):
    s = ""
    for i in range(len(self.items)):
        s += str(self.items[i].value) + "-"
    return s

Stack.__len__ = __len__
Stack.size = size
Stack.__str__ = __str__

def reverse_level_order_print(self, start):
    if start is None:
        return

    queue = Queue()
    stack = Stack()
    queue.enqueue(start)

    traversal = ""
    while len(queue) > 0:
        node = queue.dequeue()
        stack.push(node)
        
        if node.right:
            queue.enqueue(node.right)
        if node.left:
            queue.enqueue(node.left)

    while len(stack) > 0:
        node = stack.pop()
        traversal += str(node.value) + "-"

    return traversal

BinaryTree.reverse_level_order_print = reverse_level_order_print

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print(tree.reverse_level_order_print(tree.root))

if __name__ == "__main__":
    main()