class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,root = None):
        self.root = root


    def insert(self,data):
        node  = Node(data)
        if self.root is None:
            self.root = node
            print(f"root {data}")
        elif self.root.left is None:
            print(f"left {data}")
            self.root.left = node
        elif self.root.right is None:
            print(f"right {data}")
            self.root.right = node
        return self.root

    def inorder(self,root):
        current = root
        if current is None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)


    def preorder(self,root):
        current = root
        if current is None:
            return
        print(current.data)
        self.preorder(current.left)
        self.preorder(current.right)

    def postorder(self,root):
        current = root
        if current is None:
            return
        self.postorder(current.right)
        self.postorder(current.left)
        print(current.data)



tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)


print(f"the preorder traversal is {tree.preorder(tree.root)}")
print(f"the inorder traversal is {tree.inorder(tree.root)}")
print(f"the postorder traversal is {tree.postorder(tree.root)}")
