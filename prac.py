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
        print("preorder",node.value, end=" ")   
        bst._preorder(node.left)       
        bst._preorder(node.right)  

bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
print(bst.search(10))  
bst.preorder()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        while current:
            nxt = current.next    # save next node
            current.next = prev   # reverse pointer
            prev = current        # move prev forward
            current = nxt         # move current forward
        self.head = prev
        

linked_list = SinglyLinkedList()
linked_list.display() 