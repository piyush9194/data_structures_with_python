""" Vertical order traversal of a binary tree"""


def vertical_order_traversal(self):
    queue = []
    map = {}
    order = 0
    current = self.root
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
            queue.append([visited.right, order + 1])
        queue = queue[1:]
    map = dict(sorted(map.items()))
    print(map)