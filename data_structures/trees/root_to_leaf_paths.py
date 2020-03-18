"""
    https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/

    The idea is to maintain a path array and pathlength variable. If the length of path Array is greater than
    pathlength then insert at correct position else append. If you encounter the leaf node print all the elements
    in the path till the pathlength variable else recursively calls the left and right nodes.

"""


def root_to_leaf_path(root, path=[], pathlength=0):
    if root is None:
        return None

    if len(path) > pathlength:
        path[pathlength] = root.data
    else:
        path.append(root.data)

    pathlength = pathlength + 1
    if root.left is None and root.right is None:
        count = pathlength
        for items in path:
            if count > 0:
                print(items, end=" ")
            count = count - 1
        print('#', end="")
    else:
        root_to_leaf_path(root.left, path, pathlength)
        root_to_leaf_path(root.right, path, pathlength)
