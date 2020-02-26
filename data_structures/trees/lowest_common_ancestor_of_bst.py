""" Find the Lowest Common Ancestor of a Binary Search Tree. """


def LCA(root, n1, n2):
    if root is None:
        return None
    if root and root.key > max(n1, n2):
        return LCA(root.left, n1, n2)
    elif root and root.key < min(n1, n2):
        return LCA(root.right, n1, n2)
    else:
        return root.key


