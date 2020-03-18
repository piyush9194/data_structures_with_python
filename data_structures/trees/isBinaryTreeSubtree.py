class Solution:
    def isSubtree(self, s, t) -> bool:
        def isIdentical(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return root1.val == root2.val and isIdentical(root1.left, root2.left) and isIdentical(root1.right,
                                                                                                  root2.right)

        if t is None:
            return True
        if s is None:
            return False

        if isIdentical(t, s):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)