"""":arg
In a given grid, each cell can have one of three values:\
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""


class Solution:
    def orangesRotting(self, grid):

        row = len(grid)
        col = len(grid[0])
        queue = []
        fresh = 0
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 2:
                    pos = [i, j]
                    queue.append(pos)
                if grid[i][j] == 1:
                    fresh += 1
        print(queue, fresh)
        answer = 0

        while queue and fresh > 0:
            length = len(queue)
            while length > 0:
                current = queue[0]

                i = current[0]
                j = current[1]

                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    queue.append([i - 1, j])
                    fresh = fresh - 1
                if i + 1 < row and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    queue.append([i + 1, j])
                    fresh = fresh - 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    queue.append([i, j - 1])
                    fresh = fresh - 1
                if j + 1 < col and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    queue.append([i, j + 1])
                    fresh = fresh - 1

                queue = queue[1:]
                length = length - 1
            answer += 1
            print(queue, fresh, answer)

        if fresh == 0:
            return answer
        else:
            return -1



