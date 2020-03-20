"""
Spiral order traversal of tree
https://www.youtube.com/watch?v=YgL-AhYpkIE&list=PLjhq5EHRYAeJclFmYCD4Q2YOWJP68X244&index=9
"""


def spiral_order_traversal(self):
    current = self.root
    stack_1 = []
    stack_2 = []
    stack_1.append(current)
    while stack_1 or stack_2:
        while stack_1:
            visited = stack_1[-1]
            if visited.left:
                stack_2.append(visited.left)
            if visited.right:
                stack_2.append(visited.right)
            print(visited.data, end=' ')
            stack_1.pop()

        while stack_2:
            visited = stack_2[-1]
            if visited.left:
                stack_1.append(visited.right)
            if visited.right:
                stack_1.append(visited.left)
            print(visited.data, end=' ')
            stack_2.pop()


""""Other method using the property of even and odd"""

def printSpiral(root):
    if root is None:
        return
    # Code here
    current = root
    queue= []
    level = 0
    queue.append(current)
    while queue:
        result = []
        count = len(queue)
        while count>0:
            visited = queue[0]
            result.append(visited.data)
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)
            queue=queue[1:]
            count=count-1
        if level %2 !=0:
            for items in result:
                print(items,end=" ")
        else:
            for items in reversed(result):
                print(items,end = " ")
        level = level+1