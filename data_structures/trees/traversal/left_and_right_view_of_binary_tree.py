def left_view_of_tree(self):
    current = self.root
    queue = []
    queue.append(current)
    while queue:
        count = count2 = len(queue)

        while count > 0:
            visited = queue[0]
            if count2 == len(queue):
                temp = visited.data
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)

            queue = queue[1:]
            count = count - 1
        print(temp, end=' ')


def rightView(root):
    if root is None:
        return
    current = root
    queue = []
    queue.append(current)
    while queue:
        count = len(queue)
        while count>0:
            visited = queue[0]
            temp = visited.data
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)

            queue = queue[1:]
            count = count -1
        print(temp,end = ' ')