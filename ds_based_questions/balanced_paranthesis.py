class Node():
    def __init__(self, value):
        self.next = None
        self.value = value


class Solution(object):

    def __init__(self, head=None):
        self.head = head

    def push(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        current = self.head
        self.head = current.next
        current.next = None

    def length(self):
        count = 0
        current  = self.head
        while current:
            current = current.next
            count = count +1
        return count



    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = s
        if data == '':
            return True
        data = [items for items in data]
        opening_par = ['(', '{', '[']
        closing_par = [')', '}', ']']
        for item in data:
            if item in opening_par:
                self.push(item)
            elif item in closing_par:
                if self.length() == 0:
                    return False
                self.push(item)
                current = self.head
                next_element = self.head.next
                if current.value == '}' and next_element.value == '{' \
                        or current.value == ')' and next_element.value == '(' \
                        or current.value == ']' and next_element.value == '[':
                    self.pop()
                    self.pop()

                else:
                    return False
        if self.length() == 0:
            return True
        else:
            return False


# a = Solution()
# print(a.isValid(']'))





"""List implementation"""


class Solution:

    def isValid(self, s: str) -> bool:
        balanced = True
        list = []

        for item in s:
            if balanced is True:
                if len(s) == 0:
                    return balanced
                elif item in (']', '}', ')') and len(list) == 0:
                    balanced = False
                    return balanced

                elif item in ('(', '{', '['):
                    list.append(item)
                elif item in (']', '}', ')'):
                    last_item = list[-1]
                    if item == ']' and last_item == '[':
                        list.pop()
                    elif item == '}' and last_item == '{':
                        list.pop()
                    elif item == ')' and last_item == '(':
                        list.pop()
                    else:
                        balanced = False

        if len(list) == 0:
            balanced = True
        else:
            balanced = False

        return balanced





a=Solution()

print(a.isValid("{"))





