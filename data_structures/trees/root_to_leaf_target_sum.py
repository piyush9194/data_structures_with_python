""" Check if a given binary tree has a path whose sum is equal to the given sum"""


def checkSumPath(self, root, path, pathlength, val):
    if root is None:
        return None

    if len(path) > pathlength:
        path[pathlength] = root.data
    else:
        path.append(root.data)

    pathlength = pathlength + 1
    if root.left is None and root.right is None:
        if sum(path) == val:
            print(f"The path leading to sum: {val} is {path}")

    self.checkSumPath(root.left, path, pathlength, val)
    self.checkSumPath(root.right, path, pathlength, val)