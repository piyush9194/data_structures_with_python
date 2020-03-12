"""" Print the bottom view of the binary tree
     https://www.youtube.com/watch?v=ZyWh2v-74QI&list=PLjhq5EHRYAeLdh0xtn2v7wbQsVc8WAB2e&index=10
"""

from collections import OrderedDict

def bottom_view_of_binary_tree(self):
    current = self.root
    if current is None:
        return None
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
            queue.append([visited.right, order + 1])
        queue = queue[1:]

    map = dict(sorted(map.items()))
    for k, v in map.items():
        print(v[-1], end=' ')