""""
  In breadth first search traversal you visit all the nodes at each level print them and
  move to the next level. This can be implemeted with the help of the queueu data structure
  you have studied before.

"""

class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)


    def dequeue(self):
        if len(self.items) >0:
            return (self.items.pop(0))

    def peek(self):
        return self.items[0].data




class BinaryTree(TreeNode):
    def __init__(self,root=None):
        self.root = root

    def insert(self,data):
        node  = TreeNode(data)
        if self.root is None:
            self.root = node
        elif self.root.left is None:
            self.root.left = node
        elif self.root.right is None:
            self.root.right = node
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            current.left = node
        return self.root

    def inorder(self,root):
        current = root
        if current is None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

    def breadth_first_search_traversal(self,root):
        queue = Queue()
        traversal = " "
        if root is None:
            return
        else:
            queue.enqueue(root)
            while len(queue.items)>0:
                traversal = traversal + "-->" + str(queue.peek())
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(root.right)

        return traversal

    def height_of_tree(self,root):
        if root is None:
            return -1
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        return 1 + max (left_height,right_height)


tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)



print(f"the inorder traversal is")
tree.inorder(tree.root)
print(f" the breadth first search is {tree.breadth_first_search_traversal(tree.root)}")
print(f" The height of the tree is {tree.height_of_tree(tree.root)}")


"""
   10
20    30   
40
50


10                       10 
20 30                    10 20
30 40                    10 20 30
40 50                    10 20 30 40
50                       10 20 30 40 50
"""