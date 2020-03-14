"""The idea behind boundary traversal of binary tree is get the left view of the tree
   and the right view of the tree and the leaf nodes and remove the common nodes, reverse the right view
   and print the output in order[left,leaf,right]

   special cases left to root is empty or right to root is empty
   """


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
        count1 = count2 = len(queue)
        while count1 > 0:
            visited = queue[0]
            if count2 == count1:
                left = visited
            right = visited
            count1 = count1 - 1
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
    boundary = left_view + leaves + right_view[:-1]
    for nodes in boundary:
        print(nodes.data, end=" ")

