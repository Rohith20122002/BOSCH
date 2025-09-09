class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def preorder(self):
        return self._preorder(self.root)
    def _preorder(self,node):
     if node:
        print(node.value)   
        bst._preorder(node.left)       
        bst._preorder(node.right)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.preorder()