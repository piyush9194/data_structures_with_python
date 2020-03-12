class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,root = None):
        self.root = root

    def print(self,a,b,c):
        print("hello")




    def insert(self,root,data):
        current = root
        node  = Node(data)
        if self.root is None:
            self.root = node
        elif data < current.data:
            if current.left:
                self.insert(current.left,data)
            else:
                current.left = node
        elif data > current.data:
            if current.right:
                self.insert(current.right,data)
            else:
                current.right = node

    def inorder(self,root):
        current = root
        if current:
            self.inorder(current.left)
            print(current.data, end=' ')
            self.inorder(current.right)



    def preorder(self,root):
        current = root
        if current:
            print(current.data, end=' ')
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self,root):
        current = root
        if current:
            self.postorder(current.right)
            self.postorder(current.left)
            print(current.data, end=' ')

    def reverse_level_order_traversal(self):
        current = self.root
        queue  = []
        stack = []
        queue.append(current)
        while queue:
            visited = queue[0]
            stack.append(visited.data)
            if visited.right:
                queue.append(visited.right)
            if visited.left:
                queue.append(visited.left)
            queue = queue[1:]

        # output = list(reversed(stack))
        for item in stack[::-1]:
            print(item,end=' ')




tree = BinaryTree()
tree.insert(tree.root,30)
tree.insert(tree.root,20)
tree.insert(tree.root,40)
tree.insert(tree.root,15)
tree.insert(tree.root,25)
tree.insert(tree.root,35)
tree.insert(tree.root,45)


tree.preorder(tree.root)
print("\n")
tree.inorder(tree.root)
print("\n")
tree.postorder(tree.root)

print("\n The level order traversal is : ")
tree.reverse_level_order_traversal()
