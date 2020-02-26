"""
Find the LCA of Binary Tree.


https://www.youtube.com/watch?v=13m9ZCB8gjw
"""

def lca(root, n1, n2):

    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    node_left = lca(root.left, n1, n2)
    node_right = lca(root.right, n1, n2)

    if node_left is not None and node_right is not None:
        return root
    if node_left is None and root.right is None:
        return None

    return node_left if node_left is not None else node_right
