""""
        Check if a given trees follows the BST property i.e each and every node on the left is smaller than
        the current node and each and every node on the right is larger than the current node.If every node
        follows this property then the trees is said to be follow the BST property.
"""



def isBST(root,min, max):
    if root is None:
        return True

    if root.data < min or root.data > max:
        return False
    else:
        return(isBST(root.left) and isBST(root.right))


