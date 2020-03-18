def root_to_leaf_path_and_sum(self, root, path=[], pathlength=0, final_result={}):
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
        data = " "
        for items in path:
            if count > 0:
                # print(items, end=" ")
                data = data + str(items) + "-->"
                sum = sum + items
            count = count - 1
        final_result[sum] = data

    else:
        self.root_to_leaf_path_and_sum(root.left, path, pathlength, final_result)
        self.root_to_leaf_path_and_sum(root.right, path, pathlength, final_result)

    result = max(final_result, key=int)
    print(final_result)

    return final_result[result]