""""A stack is a data struture in which insertion and deletion can happen only at the
    begining. Its a useful data structure in breadth first search.
 """


class Node():
    def __init__(self,value):
        self.next = None
        self.value = value


class Stack():

    def __init__(self,head=None):
        self.head = head


    def push(self,items):

        for value in items:
            node = Node(value)

            if self.head is None:
                self.head = node
            else:
                node.next = self.head
                self.head = node

    def pop(self):
        current = self.head
        self.head = current.next

    def traverse(self):
        current =self.head
        data = ''
        while current.next:
            data = data + "-->" + str(current.value)
            current=current.next
        print(data)


plates = Stack()
plates.push([10,20,30,40,50])
plates.traverse()
plates.pop()
plates.traverse()


