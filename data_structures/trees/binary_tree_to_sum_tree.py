"""Convert a binary tree to its sum tree
  Get the value of the tree in a temp variable and recursively call the left and the right child.
"""


def convert_binary_tree_to_sum_tree(self, root):
    if root is None:
        return 0

    temp = root.data

    root.data = self.convert_binary_tree_to_sum_tree(root.left) + self.convert_binary_tree_to_sum_tree(root.right)

    return temp + root.data