def diagonalSum(root):
    #:param root: root of the given tree.
    # code here

    current = root
    queue = []
    order = 0
    map = OrderedDict()
    queue.append([current, order])
    while queue:
        visited = queue[0][0]
        order = queue[0][1]
        if order not in map:
            map[order] = [visited.data]
        else:
            map[order].append(visited.data)
        if visited.left:
            queue.append([visited.left, order - 1])
        if visited.right:
            queue.append([visited.right, order])
        queue = queue[1:]
    for k, v in map.items():
        print(sum(v), end=" ")