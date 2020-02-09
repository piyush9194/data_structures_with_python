class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class CircularQueue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.next = None


    def enqueue(self,data):
        for items in data:

            node = Node(items)
            if self.front is None:
                self.front = node
            else:
                self.rear.next = node

            self.rear = node
            self.rear.next = self.front
                

    def dequeue(self):
        if self.tail is not None:
            current = self.tail
            delete = self.tail
            current_next = self.tail.next
            while current.next != self.tail:
                current = current.next
            current.next = current_next
            delete.next = None
            self.tail = current_next

    def traverse(self):
        print(f"the front value is {self.front.value}{self.front}")
        print(f"the rear value is {self.rear.value}{self.rear}{self.rear.next}")
        current = self.front
        data = ""
        while current.next != self.front:
            data = data + "-->" + str(current.value)
            current = current.next
        data = data +   "-->" + str(current.value)
        print(f"The circular queue is {data}")


if __name__ == "__main__":
    queue = CircularQueue()
    queue.enqueue([10,20])
    queue.traverse()
