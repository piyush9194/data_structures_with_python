""""
   Implement a binary search trees.
        Insertion : O(logn)     Worst Case: O(n)
        Deletion: O(logn)       Worst Case: O(n)
        Search:   O(logn)       Worst Case: O(n)

"""


class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self,root=None):
        self.root = root


    def insert(self,data,root):
        # print(f"data inseretd is {data}")
        node = TreeNode(data)
        current = root
        if self.root is None:
            self.root = node
        elif data <= current.data:
            if current.left is None:
                current.left = node
            else:
                self.insert(data,current.left)
        elif data> current.data:
            if current.right is None:
                current.right = node
            else:
                self.insert(data,current.right)


    def inorder_traversal(self,root):
        traversal = " "
        current = root

        if current is None:
            return
        else:
            self.inorder_traversal(current.left)
            print(current.data)
            self.inorder_traversal(current.right)


    def desc_traversal(self,root):
        traversal = " "
        current = root

        if current is None:
            return
        else:
            self.desc_traversal(current.right)
            print(current.data)
            self.desc_traversal(current.left)




tree = BinarySearchTree()
tree.insert(9,tree.root)
tree.insert(5,tree.root)
tree.insert(6,tree.root)
tree.insert(15,tree.root)
tree.insert(10,tree.root)
tree.insert(4,tree.root)
tree.insert(40,tree.root)

# trees.inorder_traversal(trees.root)

tree.desc_traversal(tree.root)









