"""Use a queue to trvaerse in level order traversal and use the stack to hold the elements."""

def reverse_level_order_traversal(self):
    current = self.root
    queue = []
    stack = []
    queue.append(current)
    while queue:
        visited = queue[0]
        stack.append(visited.data)
        if visited.right:
            queue.append(visited.right)
        if visited.left:
            queue.append(visited.left)
        queue = queue[1:]

    # output = list(reversed(stack))
    for item in stack[::-1]:
        print(item, end=' ')
