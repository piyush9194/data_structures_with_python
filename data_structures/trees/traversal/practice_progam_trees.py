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

    def boundary_traversal_of_binary_tree(self):
        self.result = []
        leaf = []
        def leaf_nodes(root):
            if root:
                leaf_nodes(root.left)
                if root.left is None and root.right is None:
                    leaf.append(root)
                leaf_nodes(root.right)
            return leaf

        queue = []
        current = self.root
        queue.append(current)
        left_view = []
        right_view = []
        while queue:
            count1=count2 = len(queue)
            while count1>0:
                visited = queue[0]
                if count2 == count1:
                    left= visited
                right = visited
                count1 = count1 -1
                queue = queue[1:]
                if visited.left:
                    queue.append(visited.left)
                if visited.right:
                    queue.append(visited.right)

            left_view.append(left)
            right_view.append(right)

        if self.root.right is None:
            right_view = [self.root]
        else:
            right_view.reverse()

        if self.root.left is None:
            left_view = [self.root]

        leaves = leaf_nodes(self.root)

        for items in leaf:
            if items in left_view:
                left_view.remove(items)
            if items in right_view:
                right_view.remove(items)
        boundary = left_view + leaves+right_view[:-1]
        for nodes in boundary:
            print(nodes.data, end = " ")



    def diameter_of_binary_tree(self,root):
        self.diameter = 0
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            c_diameter = left + right
            self.diameter = max(self.diameter, c_diameter)

            return max(left, right) + 1

        height(root)
        return self.diameter



    def height_of_tree(self,root):
        current = root
        if current is None:
            return -1
        else:
            return 1 + max(self.height_of_tree(current.left), self.height_of_tree(current.right))
        
    def number_of_nodes(self,root):
        
        if root is None:
            return 0
        else:
            return 1 + self.number_of_nodes(root.left) + self.number_of_nodes(root.right)

    def number_of_leaf_nodes(self,root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        return self.number_of_leaf_nodes(root.left) + self.number_of_leaf_nodes(root.right)


    def number_of_full_nodes(self,root,list_a=[]):
        if root is None:
            return 0
        else:
            self.number_of_full_nodes(root.left,list_a )
            if root.left is not None and root.right is not None:
                list_a.append(root.data)
                print(root.data,list_a)
            self.number_of_full_nodes(root.right,list_a)

        return len(list_a)


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
        map = OrderedDict(sorted(map.items()))
        print(map)
        list_a = []
        for k,v in map.items():
            list_a.append(v)

        print(list_a)

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

    def spiral_order_traversal(self):
        current = self.root
        queue_1 = []
        queue_2 = []
        queue_1.append(current)
        while queue_1 or queue_2:
            while queue_1:
                visited = queue_1[-1]
                if visited.left:
                    queue_2.append(visited.left)
                if visited.right:
                    queue_2.append(visited.right)
                print(visited.data, end=' ')
                queue_1.pop()


            while queue_2:
                visited = queue_2[-1]
                if visited.left:
                    queue_1.append(visited.right)
                if visited.right:
                    queue_1.append(visited.left)
                print(visited.data, end=' ')
                queue_2.pop()

    def print_and_count_leaf_nodes(self,root):
        current = root
        if current is None:
            return 0
        if current.left is None and current.right is None:
            print(current.data, end = ' ')
            return 1
        else:
            return self.count_leaf_nodes(current.left) + self.count_leaf_nodes(current.right)

    def lowest_common_ancestor(self,root,n1,n2):
        current = root
        if current is None:
            return None

        if current.data == n1 or current.data == n2:
            return current

        left = self.lowest_common_ancestor(current.left,n1,n2)
        right = self.lowest_common_ancestor(current.right,n1,n2)

        if left is None and right is None:
            return None
        if left is not None and right is not None:
            return current

        return left if left else right


    def mirror_image_of_tree(self,root):
        """Swap every node left and right child in postorder traversal"""
        current = root
        if current:
            self.mirror_image_of_tree(current.left)
            self.mirror_image_of_tree(current.right)
            current.left, current.right = current.right, current.left


    def right_view_of_tree(self):
        current = self.root
        queue = []
        queue.append(current)
        while queue:
            count = len(queue)
            while count>0:
                visited = queue[0]
                temp = visited.data
                if visited.left:
                    queue.append(visited.left)
                if visited.right:
                    queue.append(visited.right)

                queue = queue[1:]
                count = count -1
            print(temp,end = ' ')

    def left_view_of_tree(self):
        current = self.root
        queue = []
        queue.append(current)
        while queue:
            count=count2 = len(queue)

            while count>0:
                visited = queue[0]
                if count2 == len(queue) :
                    temp = visited.data
                if visited.left:
                    queue.append(visited.left)
                if visited.right:
                    queue.append(visited.right)

                queue = queue[1:]
                count = count -1
            print(temp,end = ' ')

    def diagonal_view_of_tree(self):

        current = self.root
        if current is None:
            return
        queue = [ ]
        map = OrderedDict()
        order = 0
        queue.append([current,order])

        while queue:
            visited = queue[0][0]
            order = queue[0][1]
            if order not in map.keys():
                map[order] = [visited.data]
            else:
                map[order].append(visited.data)
            if visited.left:
                queue.append([visited.left, order-1])
            if visited.right:
                queue.append([visited.right, order])
            queue = queue[1:]

        print(map)
        for k,v in map.items():
            print(v,sum(v))


    def bottom_view_of_binary_tree(self):
        current = self.root
        if current is None:
            return None
        queue = []
        map = OrderedDict()
        order = 0
        queue.append([current,order])
        while queue:
            visited = queue[0][0]
            order = queue[0][1]
            if order not in map.keys():
                map[order] = [visited.data]
            else:
                map[order].append(visited.data)
            if visited.left:
                queue.append([visited.left, order -1])
            if visited.right:
                queue.append([visited.right, order +1])
            queue = queue[1:]

        map = dict(sorted(map.items()))
        for k, v in map.items():
            print(v[-1], end=' ')




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
tree.insert(tree.root,50)


# tree.inorder_traversal(tree.root)


# print(tree.isBST())

# tree.topView(tree.root)

# tree.level_order_traversal()
# #
# #
# tree.vertical_order_traversal()
#
# tree.top_view_of_tree()

# tree.spiral_order_traversal()

# print("\n" + str(tree.count_leaf_nodes(tree.root)))


# print(tree.lowest_common_ancestor(tree.root, 5,15).data)

# tree.mirror_image_of_tree(tree.root)

# tree.level_order_traversal()


# print("Right view of tree")
# tree.right_view_of_tree()
# print("\n")
# print("Left view of tree")
# tree.left_view_of_tree()

# tree.diagonal_view_of_tree()

# tree.bottom_view_of_binary_tree()

# print(tree.height_of_tree(tree.root))


# print("The number of nodes in the tree: ")

# print(tree.number_of_nodes(tree.root))

# print(tree.number_of_leaf_nodes(tree.root))

# print(tree.number_of_full_nodes(tree.root))


# print(tree.diameter_of_binary_tree(tree.root))

tree.boundary_traversal_of_binary_tree()