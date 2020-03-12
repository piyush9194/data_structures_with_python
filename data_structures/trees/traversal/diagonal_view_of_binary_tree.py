from collections import OrderedDict

def diagonal_view_of_tree(self):
    current = self.root
    if current is None:
        return
    queue = []
    map = OrderedDict()
    order = 0
    queue.append([current, order])

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
            queue.append([visited.right, order])
        queue = queue[1:]

    print(map)
    for k, v in map.items():
        print(v)