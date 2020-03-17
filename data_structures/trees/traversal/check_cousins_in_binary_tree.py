class Solution:
    def isSibling(self, root, a, b):
        if root:
            if root.left is not None and root.right is not None:
                if root.left.val == a and root.right.val == b or root.left.val == b and root.right.val == a:
                    return True
            return self.isSibling(root.left, a, b) or self.isSibling(root.right, a, b)

    def isCousins(self, root, x, y):
        current = root
        queue = []
        queue.append(current)
        answer = False
        while queue:
            count = len(queue)
            level = []
            while count > 0:
                visited = queue[0]
                level.append(visited.val)
                if visited.left:
                    queue.append(visited.left)
                if visited.right:
                    queue.append(visited.right)
                queue = queue[1:]
                count = count - 1
            if x in level and y in level and self.isSibling(root, x, y) is not True:
                answer = True
        return answer