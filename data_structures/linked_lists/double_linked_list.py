class Node():

    def __init__(self,value):
        self.next = None
        self.prev = None
        self.value = value


class DoublyLinkedlist(Node):

    def __init__(self, head=None):
        self.head = head


    def append_at_beg(self,value):

        node = Node(value)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            node.next = current
            current.prev = node
            self.head = node


    def append_at_end(self,value):
        node =Node(value)
        current = self.head

        if self.head is None:
            self.head = node

        else:
            while current.next:
                current = current.next

            current.next = node
            node.prev = current

    def traverse(self):
        current = self.head
        linked_list = ''
        while current:
            linked_list = linked_list + "->" + str(current.value)
            current = current.next
        print(linked_list)


stack=DoublyLinkedlist()
stack.append_at_beg(10);stack.append_at_beg(20);stack.append_at_beg(30);stack.append_at_beg(40);
stack.append_at_beg(50);stack.append_at_beg(60)
stack.traverse()


queue=DoublyLinkedlist()
queue.append_at_end(10);queue.append_at_end(20);queue.append_at_end(30);
queue.append_at_end(40);queue.append_at_end(50);queue.append_at_end(60)
queue.traverse()