from binary_tree import *

def preorder_print(self, root):
    nodes = []
    nodes.append(root)
    while (len(nodes) > 0):
        node = nodes.pop()
        print(node.value, end=" ")
        if node.right is not None:
            nodes.append(node.right)
        if node.left is not None:
            nodes.append(node.left)
BinaryTree.preorder_print = preorder_print

def inorder_print(self, root):
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right
        else:
            break
   
BinaryTree.inorder_print = inorder_print

def postorder_print(self, root):
    if root is None:
        return       
     
    s1 = []
    s2 = []
    s1.append(root)

    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
 
    while s2:
        node = s2.pop()
        print(node.value,end=" ")
BinaryTree.postorder_print = postorder_print

# Helper method
def print_tree(self, tree, traversal_type):
    if traversal_type == "preorder":
        return self.preorder_print(tree.root)
    elif traversal_type == "inorder":
        return self.inorder_print(tree.root)
    elif traversal_type == "postorder":
        return self.postorder_print(tree.root)
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

    # output must be:
    # 1-2-4-5-3-6-7-    preorder
    # 4-2-5-1-6-3-7-    inorder
    # 4-5-2-6-7-3-1-    postorder

if __name__ == "__main__":
    main()