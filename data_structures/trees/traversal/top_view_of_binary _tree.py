"""For a given tree print the top view"""


def topView(root):
    '''
    :param root: root of the binary tree
    :return: None, newline is provided by driver code
    '''
    # code here

    if root is None:
        return
    order = 0
    current = root
    queue = []
    map = {}
    queue.append([current,order])
    while queue:
        visited = queue[0][0]
        order  = queue[0][1]
        if int(order) not in map:
            map[int(order)] = [visited.info]
        else:
            map[int(order)].append(visited.info)

        if visited.left:
            queue.append([visited.left,int(order -1)])
        if visited.right:
            queue.append([visited.right , int(order+1)])
        queue = queue[1:]
    map= dict(sorted(map.items()))
    # print(map)
    for k,v in map.items():
        print(v[0],end=' ')
