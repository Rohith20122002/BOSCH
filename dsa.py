


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new

    def print(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

    def target(self,data):
        current=self.head
        while current is not None:
            if(data==current.data):
                print("found")
                return 
            else:
                print("not found")
            current=current.next
        
    def ibeg(self,node):
        new=Node(node)
        new.next=self.head
        self.head=new

    def  iend(self,node):
        new=Node(node)
        current=self.head
        while current.next is not None:
            current =current.next
        current.next=new
        self.head=current


ll=linkedlist()
ll.insert(10)
ll.insert(20)
ll.print()
ll.target(10)
ll.ibeg(20)
ll.print()
ll.iend(50)
ll.print()

