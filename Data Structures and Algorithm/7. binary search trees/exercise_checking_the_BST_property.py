from binary_search_tree import Node,BST

# i came up with this one (the course give the implementation after this one)
# the base idea is using the same algorithm as level-order traversal (but i'm not sure about this one)
def is_bst_satisfied(self, start):
    if start is None:
        return False

    queue = []
    queue.insert(0, start)

    traversal = ""
    while len(queue) > 0:
        node = queue.pop()
        data = node.data

        if node.left:
            if data < node.left.data: return False
            queue.insert(0, node.left)
        if node.right:
            if data > node.right.data: return False
            queue.insert(0, node.right)
    
    return True

# the course implementation:

# the base idea is to use in-order traversal
# this algorithm used because the algorithm output the sorted BST (if the BST property satisfied)
def is_bst_satisfied(self):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True         # the course said when it is empty, return True
        
        val = node.data
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    if self.root:
        return helper(self.root)
    else:
        return False

BST.is_bst_satisfied = is_bst_satisfied

def main():
    bst = BST(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(5)
    bst.insert(10)

    tree = BST(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(8)

    print(bst.is_bst_satisfied())
    print(tree.is_bst_satisfied())

if __name__ == "__main__":
    main()