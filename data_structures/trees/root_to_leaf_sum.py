def root_to_leaf_path(self, root, path=[], pathlength=0):
    if root is None:
        return None

    if len(path) > pathlength:
        path[pathlength] = root.data
    else:
        path.append(root.data)

    pathlength = pathlength + 1
    if root.left is None and root.right is None:
        count = pathlength
        sum = 0
        for items in path:
            if count > 0:
                # print(items, end=" ")
                sum = sum + items
            count = count - 1
        print(f"Sum is {sum}", end=" ")
        print(' ')
    else:
        self.root_to_leaf_path(root.left, path, pathlength)
        self.root_to_leaf_path(root.right, path, pathlength)