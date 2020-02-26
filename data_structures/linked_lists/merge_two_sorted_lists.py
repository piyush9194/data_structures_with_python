"""Write a program to merge two sorted linked lists and return the head of the sorted Linked List"""
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def mergeLists(head1, head2):
    current1 = head1
    current2 = head2

    final_list = SinglyLinkedList()

    while current1 or current2:
        if current1 and current2:
            if current2.data <= current1.data:
                final_list.insert_node(current2.data)
                current2 = current2.next
            elif current2.data >= current1.data:
                final_list.insert_node(current1.data)
                current1 = current1.next
        elif current1:
            final_list.insert_node(current1.data)
            current1 = current1.next
        elif current2:
            final_list.insert_node(current2.data)
            current2 = current2.next
    return final_list.head
