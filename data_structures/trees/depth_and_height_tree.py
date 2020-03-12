
"""Calculate the height of the binary tree
"""

def height_of_tree(self, root):
    current = root
    if current is None:
        return -1
    else:
        return 1 + max(self.height_of_tree(current.left), self.height_of_tree(current.right))
