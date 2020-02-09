class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():

    def __init__(self,head = None):
        self.head = head
        self.count = 0
        self.min = None

    def push(self,data):
        for item in data:
            node = Node(item)

            if self.head is None:
                self.head = node
                self.min = node.value
            else:
                node.next = self.head
                self.head = node
            self.count = self.count + 1

            if item <= self.min:
                self.min = item


    def pop(self):
        if self.head is not None:
            current = self.head
            self.head = current.next
            current.next = None

        self.count = self.count -1

    def traverse(self):
        current = self.head
        data = ""
        while current is not None:
            data = data + str(current.value)
            current=current.next

        print(f"the stack is {data}")

    def convert_to_binary(self,num):
        while num>0:
            bit = num%2
            num = int(num/2)
            self.push([bit])
        print(f"the length of the stack is {self.count}")


if __name__=="__main__":
    stack = Stack()
    # stack.convert_to_binary(20)
    # stack.traverse()

    stack.push([10,20,30,40,50])
    print(f"the min element is {stack.min} ")







