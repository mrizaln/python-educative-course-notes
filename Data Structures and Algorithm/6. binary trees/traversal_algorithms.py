from binary_tree import *

# Tree Traversal is the process of visiting (checking or updating) each node in a tree data structure, exactly once. 
# Trees may be traversed in multiple ways: depth-first or breadth-first order.
# There are three common ways to traverse a tree in depth-first order:
    # In-order
    # Pre-order
    # Post-order

# Pre-order Traversal
    # Check if the current node is empty/null.
    # Display the data part of the root (or current node).
    # Traverse the left subtree by recursively calling the pre-order method.
    # Traverse the right subtree by recursively calling the pre-order method.
def preorder_print(self, start, traversal):
    """Root->Left->Right"""
    if start:
        traversal += (str(start.value) + "-")
        traversal = self.preorder_print(start.left, traversal)
        traversal = self.preorder_print(start.right, traversal)
    return traversal
BinaryTree.preorder_print = preorder_print

# In-order Traversal#
#     Check if the current node is empty/null.
#     Traverse the left subtree by recursively calling the in-order method.
#     Display the data part of the root (or current node).
#     Traverse the right subtree by recursively calling the in-order method.
def inorder_print(self, start, traversal):
    """Left->Root->Right"""
    if start:
        traversal = self.inorder_print(start.left, traversal)
        traversal += (str(start.value) + "-")
        traversal = self.inorder_print(start.right, traversal)
    return traversal
BinaryTree.inorder_print = inorder_print

# Post-order Traversal#
#     Check if the current node is empty/null.
#     Traverse the left subtree by recursively calling the post-order method.
#     Traverse the right subtree by recursively calling the post-order method.
#     Display the data part of the root (or current node).
def postorder_print(self, start, traversal):
    """Left->Right->Root"""
    if start:
        traversal = self.postorder_print(start.left, traversal)
        traversal = self.postorder_print(start.right, traversal)
        traversal += (str(start.value) + "-")
    return traversal
BinaryTree.postorder_print = postorder_print

# Helper method
def print_tree(self, tree, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
BinaryTree.print_tree = print_tree
            
def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    #               1
    #           /       \  
    #          2          3  
    #         /  \      /   \
    #        4    5     6   7 

    for i in ("preorder", "inorder", "postorder"):
        print(tree.print_tree(tree, i))

if __name__ == "__main__":
    main()