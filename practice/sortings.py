def linear(a,m):
    for i in range(len(a)):
        if(m==a[i]):
           print("target found")
        else:
            print("not found")
m=30
linear(a,m)

def binary_search(a, target):
    a.sort()  # If your list is not sorted already
    left, right = 0, len(a) - 1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == target:
            print("target found at index", mid)
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print("target not found")
    return -1

# Example usage:
a = [10, 3, 6, 8, 2]
m = 6
binary_search(a, m)






a=[1,3,2,4,85,34,7,8]
print(a)
def bubble(a):
    for i in range(0,len(a)):
        for i in range(0,len(a)-1):
            if(a[i]>a[i+1]):
               a[i],a[i+1]=a[i+1],a[i]
    print(a)
bubble(a)


a=[1,3,2,4,85,34,7,8]
def selection(a):
    for i in range(0,len(a)):
        for i in range(0,len(a)-1):
            if(a[i]>a[i+1]):
               a[i+1],a[i]=a[i],a[i+1]
    print(a)
selection(a)

stack = []
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)
topElement = stack[-1]
print("Peek: ", topElement)
poppedElement = stack.pop()
print("Pop: ", poppedElement)
print("Stack after Pop: ", stack)
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)
print("Size: ",len(stack))




queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)
frontElement = queue[0]
print("Peek: ", frontElement)
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)
print("Queue after Dequeue: ", queue)
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)
print("Size: ", len(queue))
 


def decerator(func):
    def wrapper():
        print("before")
        samp()
        print("after")
    return wrapper



@decerator
def samp():
    print("hello")

samp()