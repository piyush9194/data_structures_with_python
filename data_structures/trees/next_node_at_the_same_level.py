def find_next_node_at_the_same_level(self, val=22):
    queue = []
    current = self.root
    queue.append(current)
    while queue:
        count = len(queue)
        while count:
            visited = queue[0]
            # print(visited.data,end = ' ')
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)

            if visited.data == val and count > 1:
                return (queue[1].data)

            queue = queue[1:]
            count = count - 1
        # print("\n")