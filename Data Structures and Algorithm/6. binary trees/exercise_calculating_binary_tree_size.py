from binary_tree import *

# iterative
def size_(self, node):
    if node is None:
        return 0

    size = 0
    stack = []
    stack.append(node)

    while stack:
        node = stack.pop()
        size += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return size
BinaryTree.size_ = size_

# recursive
def size_(self, node):
    if node is None:
        return 0
    return 1 + self.size_(node.left) + self.size_(node.right)

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(tree.size_(tree.root))

if __name__ == "__main__":
    main()