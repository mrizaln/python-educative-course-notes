# A binary search tree is a tree data structure in which nodes are arranged according
# to the BST property which is as follows:

    # The value of the left child of any node in a binary search tree will be less than whatever value
    # we have in that node, and the value of the right child of a node will be greater than the value in that node.

#             8
#           /  \ 
#          3    10
#         / \     \
#        1   6     14
#           / \    /
#          4   7  13

# time complexities of BST
#   ALGORITHM       AVERAGE CASE        WORST CASE
#    search           O(logn)              O(n)
#    insert           O(logn)              O(n)
#    delete           o(logn)              O(n)

import random

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)

    def levelorder_print(self, start):
        if start is None:
            return

        queue = []
        queue.insert(0, start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue[-1].data) + "-"
            node = queue.pop()

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        
        return traversal

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal

def main():
    bst = BST(10)

    to_be_inserted = [5 ,8, 12, 11, 3]

    for n in to_be_inserted:
        bst.insert(n)

    print(to_be_inserted)
    
    print("levelorder traversal:", bst.levelorder_print(bst.root))
    print("preorder traversal  :", bst.preorder_print(bst.root, ""))
    print("inorder traversal   :", bst.inorder_print(bst.root, ""))
    print("postorder traversal :", bst.postorder_print(bst.root, ""))

    print(bst.search(11))
    print(bst.search(14))

if __name__ == "__main__":
    main()