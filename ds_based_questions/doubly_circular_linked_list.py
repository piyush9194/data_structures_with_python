"""Implement a doubly circular linked list"""


class Node():
    def __init__(self,data=None,next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleCircularLinkedList():
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
        self.count = 0


    def enqueue(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node
        else:
            self.tail.next = node
            self.head.prev = node
        node.next = self.head
        node.prev = self.tail
        self.tail = node
        self.count +=1
        return (f"The item added is: {data} ")


    def dequeue(self):
        if self.head is None:
            print("The queue is empty")
        elif self.head == self.tail:
            self.head = self.tail = None
            self.count -=1
        else:
            second_last = self.tail.prev
            second_last.next = self.head
            self.head.prev = second_last
            self.tail = second_last
            self.count -= 1


    def traverse(self):
        queue = " "
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            while current.next != self.head:
                queue = queue + "-->" + str(current.data)
                current = current.next
            queue = queue + "-->" +str(current.data)
            return queue



a= DoubleCircularLinkedList()
print(a.enqueue(10))
print(a.enqueue(20))
print(a.enqueue(30))
print(a.traverse())
print(a.count)
a.dequeue()
print(a.count)
print(a.traverse())









