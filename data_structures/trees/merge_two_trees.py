"""
    Given two binary trees and imagine that when you put one of them to cover the other,
    some nodes of the two trees are overlapped while the others are not.

    You need to merge them into a new binary tree.
    The merge rule is that if two nodes overlap, then sum node values up as the new
    value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if t1 and not t2:
            return t1
        if t2 and not t1:
            return t2

        node = TreeNode(t1.val + t2.val)

        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)

        return node