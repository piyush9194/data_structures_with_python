""""
   Implement a binary search trees.
        Insertion : O(h)     Worst Case: O(n)
        Deletion: O(h)       Worst Case: O(n)
        Search:   O(h)       Worst Case: O(n)

        where h is height of tree.

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
        node = TreeNode(data)
        current = root
        if self.root is None:
            self.root = node
        elif data <= current.data:
            if current.left:
                self.insert(data, current.left)
            else:
                current.left = node
        elif data> current.data:
            if current.right:
                self.insert(data, current.right)
            else:
                current.right = node

    def search(self,data,root):
        current = root
        if current:
            if current.data == data:
                return True
            elif data < current.data:
                return(self.search(data, current.left))
            elif data > current.data:
                return(self.search(data, current.right))
        else:
            return False

    def delete(self,data):
        self._delete(self.root,data)


    def _delete(self,current,data,parent=None,isLeft=None):
        if current:
            if current.data == data:
                print(f"deleting the key:{data}")
                if isLeft:
                    parent.left = None
                else:
                    parent.right = None
            elif data>current.data:
                self._delete(current.right,data,current,False)
            elif data < current.data and current.left:
                self._delete(current.left,data,current,True)

        else:
            print("Key not found")

    def inorder_traversal(self,root):
        current = root
        if current is None:
            return
        else:
            self.inorder_traversal(current.left)
            print(current.data,end= "--> ")
            self.inorder_traversal(current.right)


    def desc_traversal(self,root):
        current = root
        if current is None:
            return
        else:
            self.desc_traversal(current.right)
            print(current.data,end= "--> ")
            self.desc_traversal(current.left)

    def _isBST(self,root,min,max):
        current = root
        if current is None:
            return True
        elif current.data < min or current.data>max:
            return False
        else:
            return (self._isBST(current.left,min,current.data)
            and self._isBST(current.right,current.data,max))

    def isBST(self,root):
        if self.root is None:
            return True
        else:
            min = -1000000
            max = 10000000
            return(self._isBST(root,min,max))




tree = BinarySearchTree()
tree.insert(9,tree.root)
tree.insert(5,tree.root)
tree.insert(6,tree.root)
tree.insert(15,tree.root)
tree.insert(10,tree.root)
tree.insert(4,tree.root)
tree.insert(40,tree.root)

tree.inorder_traversal(tree.root)
print("/n")
tree.desc_traversal(tree.root)
print("/n")
print(tree.search(15,tree.root))
print(tree.isBST(tree.root))





