""""
    Given a binary tree, determine if it is height-balanced.
    For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node
    differ in height by no more than 1.
"""


def isBalanced(self,root) -> bool:
    def height(root):
        if root is None:
            return 0
        return 1 + max(height(root.left), height(root.right))

    if root is None:
        return True

    lh= height(root.left)
    rh =height(root.right)
    if abs(lh -rh )<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        return True

    return False