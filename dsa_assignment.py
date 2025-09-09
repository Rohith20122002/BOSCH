class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  
print(stack.peek())  






class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  
print(queue.peek())  








class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return "Node not found"
        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = SinglyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.prepend(5)
linked_list.display()  
linked_list.delete(10)
linked_list.display()  






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

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node.value == value:
            return node is not None
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    
    
    def inorder(self):
        return self._inorder(self.root)
    def _inorder(self,node):
        if node:
            bst._inorder(node.left)         
            print(node.value)   
            bst._inorder(node.right)        
 
    

    def postorder(self):
        return self._postorder(self.root)
    def _postorder(self,node):
     if node:
           
        bst._postorder(node.left)       
        bst._postorder(node.right)
        print("postorder",node.value, end=" ") 
    
    
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
bst.postorder()
bst.inorder()





