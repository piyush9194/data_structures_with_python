"""
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


def isIdentical(root1, root2):
    current1 = root1
    current2 = root2

    if current1 is None and current2 is None:
        return True

    if current1 is not None and current2 is not None:
        return (current1.data == current2.data and
                isIdentical(current1.left, current2.left)
                and isIdentical(current1.right, current2.right))
    return False