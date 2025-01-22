from collections import deque
from typing import List

direction_set = set()
for i in range(-1, 2, 1):
    for j in range(-1, 2, 1):
        if i != 0 or j != 0:
            direction_set.add((i, j))


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        1. queue, q to visit FIFO
        2. visited, to store the point has been visited
        3. start point,
        4. func:
            1. 8 directions, exclude points out of bounder
            2. exclude points have been visited
            3. exclude point_value != 0
            4. add rest points to queue and visited
            5. steps + 1
        5. return steps
        """
        n = len(grid)
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        queue = deque()
        queue.append((0,0,1))
        visited = set()
        visited.add((0, 0))

        while queue:
            x, y, steps = queue.popleft()
            if x == n - 1 and y == n - 1:
                return steps

            for x_dire, y_dire in direction_set:
                new_x, new_y = x + x_dire, y + y_dire

                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                    queue.append((new_x, new_y, steps + 1))
                    visited.add((new_x, new_y))

        return -1

if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    test = Solution()
    print(test.shortestPathBinaryMatrix(grid))
