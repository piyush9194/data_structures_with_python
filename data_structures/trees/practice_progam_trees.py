import sys
from collections import OrderedDict


class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root  = None

    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)



    def insert(self,root,data):

        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            if data <= root.data:
                if root.left:
                    self.insert(root.left,data)
                else:
                    print(f"inserting to the left :{node.data}")
                    root.left = node
            elif data > root.data:
                if root.right:
                    self.insert(root.right,data)
                else:
                    print(f"inserting to the right: {node.data}")
                    root.right = node



    def _isBST(self,root,min,max):

        if root is None:
            return True
        elif root.data < min or root.data > max:
            return False
        else:
            return (self._isBST(root.left,min,root.data) and self._isBST(root.right,root.data,max))


    def isBST(self):
        if self.root is None:
            return True
        else:
            return(self._isBST(self.root,min=-10000,max=100000))

    def topView(self,root):
        # Write your code here
        current = root
        output = ""
        while current is not None:
            output = str(current.data)+ " " + output
            current = current.left
        sys.stdout.write(str(output))
        current = root
        while current is not None:
            if current != root:
                sys.stdout.write(str(current.data) + ' ')
            current = current.right

    def level_order_traversal(self):
        queue = []
        current = self.root
        queue.append(current)
        while queue:
            count = len(queue)
            while count > 0:
                visited = queue[0]
                print(visited.data,end= ' ')
                if visited.left:
                    queue.append(visited.left)
                if visited.right:
                    queue.append(visited.right)
                queue = queue[1:]
                count-=1
            print("\n")

    def vertical_order_traversal(self):
        queue  = []
        map = {}
        order = 0
        current = self.root
        queue.append([current,order])
        while queue:
            visited = queue[0][0]
            order = queue[0][1]
            if order not in map.keys():
                map[order] = [visited.data]
            else:
                map[order].append(visited.data)

            if visited.left:
                queue.append([visited.left, order - 1])

            if visited.right:
                queue.append([visited.right, order + 1])
            queue = queue[1:]
        map = dict(sorted(map.items()))
        print(map)

    def top_view_of_tree(self):
        if self.root is None:
            return
        order = 0
        current = self.root
        queue = []
        map = {}
        queue.append([current,order])
        while queue:
            visited = queue[0][0]
            order  = queue[0][1]
            if int(order) not in map:
                map[int(order)] = [visited.data]
            else:
                map[int(order)].append(visited.data)

            if visited.left:
                queue.append([visited.left,order -1])
            if visited.right:
                queue.append([visited.right , order+1])
            queue = queue[1:]

        map= dict(sorted(map.items()))

        for k,v in map.items():
            print(v[0],end= ' ')






    def lowest_common_ancestor(self,root,n1,n2):
        if self.root == n1 or self.root == n2:
            return(self.root)
        left = root.left
        right = root.right







tree = BinarySearchTree()
tree.insert(tree.root, 10)
tree.insert(tree.root,20)
tree.insert(tree.root,8)

tree.insert(tree.root,5)
tree.insert(tree.root,9)
tree.insert(tree.root,15)
tree.insert(tree.root,22)
tree.insert(tree.root,21)
tree.insert(tree.root,25)


# tree.inorder_traversal(tree.root)


# print(tree.isBST())

# tree.topView(tree.root)

# tree.level_order_traversal()


tree.vertical_order_traversal()

tree.top_view_of_tree()