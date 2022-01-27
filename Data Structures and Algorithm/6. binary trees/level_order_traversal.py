from binary_tree import *

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

def levelorder_print(self, start):
    if start is None:
        return

    queue = Queue()
    queue.enqueue(start)

    traversal = ""
    while len(queue) > 0:
        traversal += str(queue.peek()) + "-"
        node = queue.dequeue()

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    
    return traversal

BinaryTree.levelorder_print = levelorder_print

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print(tree.levelorder_print(tree.root))

if __name__ == "__main__":
    main()