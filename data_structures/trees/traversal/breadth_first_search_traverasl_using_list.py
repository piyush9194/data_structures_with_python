"""Level Order Traversal"""

def level_order_traversal(self):
    queue = []
    current = self.root
    queue.append(current)
    while queue:
        count = len(queue)
        while count > 0:
            visited = queue[0]
            print(visited.data, end=' ')
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)
            queue = queue[1:]
            count -= 1
        print("\n")