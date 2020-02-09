""""
1. traverse a linked list
2. Remove duplicates from a linked list
3. Get the kth to last Node from a linked list
4. Delete a node from a linked list
5. Add two linked lists from left to right
e.g. 1->2->3 + 8->7 => 321+78 = 399
6. Add two linked lists from right to left
e.g. 1->2->3 + 8->7 => 123+87 = 210

Pop operation in linked list
Insert given node into the correct sorted position in the given sorted linked list
Given a linked list, change it to be in sorted order
Split the nodes of the given linked list into front and back halves
Remove duplicates from a sorted linked list
Move front node of the given list to the front of the another list
Move even nodes to the end of the list in reverse order
Split given linked list into two lists where each list containing alternating Nodes from it
Construct a linked list by merging alternate nodes of two given lists
Merge given sorted linked lists into one
Merge Sort Algorithm for Singly Linked List
Intersection of two given sorted linked lists
Reverse linked list | Part 1 (Iterative Solution)
Reverse linked list | Part 2 (Recursive Solution)
Reverse every group of k nodes in given linked list
Find K’th node from the end in a linked list
Merge alternate nodes of two linked lists into the first list
Merge two sorted linked lists from their end
Delete every N nodes in a linked list after skipping M nodes
Rearrange linked list in specific manner in linear time
Check if linked list is palindrome or not
Move last node to front in a given Linked List
Rearrange the linked list in specific manner
Detect Cycle in a linked list (Floyd’s Cycle Detection Algorithm)
Sort linked list containing 0’s, 1’s and 2’s
Stack Implementation using Linked List
Queue Implementation using Linked List
Remove duplicates from a linked list
Rearrange the linked list so that it has alternating high, low values
Rearrange a Linked List by Separating Odd Nodes from the Even Ones
Calculate height of a binary tree with leaf nodes forming a circular doubly linked list
XOR Linked List: Overview and Implementation
Convert a multilevel linked list to a singly linked list


"""


class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList(Node):

    def __init__(self,head=None):
        self.head = head


    def append(self,value):
        node= Node(value)
        current = self.head

        if self.head is None:
            # print(f"Adding first Node: {node.value}")
            self.head = node
        else:
            while current.next:
                current = current.next
            # print(f"Adding next Node: {node.value}")
            current.next = node

    def traverse(self):
        current = self.head
        linked_list = ''
        while current:
            linked_list = linked_list +"->" + str(current.value)
            current = current.next
        print(linked_list)


    def remove_duplicates(self):

        Nodes = set()
        current= self.head
        current2 = self.head.next

        while current2:
            if current2.value in Nodes:
                current.next = current2.next
                current2 = current2.next
            else:
                Nodes.add(current.value)
                current = current.next
                current2 = current2.next


    def kth_last_Node(self,k):
        current = self.head
        count = 0
        while current:
            current = current.next
            count = count+1

        print(count,k)

        current = self.head
        for i in range(count-k):
            current = current.next

        print(f"The {k}th Node is {current.value}")

    """Insert given node into the correct sorted position in the given sorted linked list"""

    def insert(self, n):
        node = Node(n)
        print(f"Inserting the Node {node.value}")
        current = self.head
        while current.next.value <= n:
            current = current.next
        node.next = current.next
        current.next = node



list = LinkedList()

list.append(30);list.append(10);list.append(20) ;list.append(30);list.append(30);list.append(30)
list.append(30);list.append(30);list.append(40);list.append(10);list.append(20)

print("original list")
list.traverse()
list.remove_duplicates()
print("dedup list")
list.traverse()
list.kth_last_Node(4)

sorted_list = LinkedList()
sorted_list.append(10);sorted_list.append(20);sorted_list.append(30);
sorted_list.append(40);sorted_list.append(50);sorted_list.append(60)
print("before inserion")
sorted_list.traverse()
sorted_list.insert(15)
sorted_list.insert(31)
print("after inserion")
sorted_list.traverse()

















