# A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child
# and the right child. Have a look at an elementary example of a binary tree:

# Terminology
    # Depth of a Node #
        # The length of the path from a node, n, to the root node. The depth of the root node is 0.
    # Height of a Tree #
        # The length of the path from n to its deepest descendant. The height of the tree itself is
        # the height of the root node, and the height of leaf nodes is always 0.

# Types of Binary Trees #
    # Complete Binary Tree #
        # In a complete binary tree, every level except possibly the last, is completely filled and
        # all nodes in the last level are as far left as possible.
    # Full Binary Tree #
        # A full binary tree (sometimes referred to as a proper or plane binary tree) is a tree in
        # which every node has either 0 or 2 children.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

if __name__ == "__main__":
    main()