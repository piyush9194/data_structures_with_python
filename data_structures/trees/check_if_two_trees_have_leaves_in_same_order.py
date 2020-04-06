"""Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

"""


def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    def inorder(root, result):
        if root:
            inorder(root.left, result)
            if root.left is None and root.right is None:
                result.append(root.val)
            inorder(root.right, result)
        return result

    result1 = inorder(root1, [])
    result2 = inorder(root2, [])
    print(result1, result2)
    if result1 == result2:
        return True
    else:
        return False