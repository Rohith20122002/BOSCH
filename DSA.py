class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def preorder(root):
    print(root.key ,end =" ")
    print(preorder(root.left))
    print(preorder(root.right))


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)
root.right.left = Node(6)
print("Preorder Traversal:")
preorder(root)



 
def inorder(root):
    if root:
        inorder(root.left)         # 1. Traverse left
        print(root.key, end=" ")   # 2. Visit root
        inorder(root.right)        # 3. Traverse right
 
print("Inorder Traversal:")
inorder(root)

        