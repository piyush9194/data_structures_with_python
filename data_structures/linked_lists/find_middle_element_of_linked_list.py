"""
   Find the middle element of linked list in the single pass. The strategy is to maintain two pointers. One fast and one
   slow poniter. Fast pointer moves by two places at a time and slow by one.


"""


def findMid(head):
    slow = head
    fast = head
    if head.next is None:
        return head
    if head.next.next is None:
        return head.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow=slow.next
    return slow