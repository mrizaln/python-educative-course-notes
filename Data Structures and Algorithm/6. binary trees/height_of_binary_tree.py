from binary_tree import *
from level_order_traversal import Queue

# Binary tree height:
    # 1) Number of nodes on the longest path from the root to the deepest node. 
    # 2) Number of edges on the longest path from the root to the deepest node.
# Second definition is used

# recursive solution
def height(self, node):
    if node is None:
        return -1

    left_height = self.height(node.left)
    right_height = self.height(node.right)

    return 1 + max(left_height, right_height)

def height_iterative(slef, node):
    if node is None:
        return -1

    queue = Queue()
    queue.enqueue(node)
    height = -1

    while True:
        node_count = len(queue)
        if node_count == 0:
            return height

        height += 1

        while node_count > 0:
            node = queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            
            node_count -= 1

BinaryTree.height = height
BinaryTree.height_iterative = height_iterative

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print(tree.height(tree.root))
    print(tree.height_iterative(tree.root))

if __name__ == "__main__":
    main()