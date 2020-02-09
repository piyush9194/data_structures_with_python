"""
            Imlement a MyQueue class which implements a queue using two stacks
"""


class Node():

    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():

    def __init__(self,head = None):
        self.head = head
        # self.count = 0

    def enqueue(self,data):
        for item in data:
            node = Node(item)

            if self.head is None:
                self.head = node
            else:
                node.next = self.head
                self.head = node
            # self.count = self.count + 1


    def pop(self):

        if self.head is not None:
            current = self.head
            self.head = current.next
            current.next = None

        # self.count = self.count -1

    def traverse(self):
        current = self.head
        data = ""
        while current is not None:
            data = data + str(current.value) + "--->"
            current=current.next

        print(f"the Stack is {data}")


    def dequeue(self,stack_b):

        print(stack_a.head.next.value)
        while stack_a.head:
            stack_b.enqueue([stack_a.head.value])
            stack_a.pop()
        stack_b.pop()


if __name__=="__main__":
    stack_a = Stack()
    stack_b = Stack()
    stack_a.enqueue([10,20,30,40])
    stack_a.traverse()

    stack_a.dequeue(stack_b)
    stack_a.traverse()
    stack_b.traverse()





