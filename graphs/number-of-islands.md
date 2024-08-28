# 🟡 Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```python
class Solution:
    @classmethod
    def bfs(cls, grid, r, c, visited):

        queue = deque()
        queue.append((r,c))
        visited.add((r,c))

        while queue:
            row, col = queue.popleft() # O(logn)
            directions = [[0,1], [1,0], [-1,0], [0,-1]]

            for dr, dc in directions:
                neighbor = (row + dr, col + dc)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) \
                and neighbor not in visited and grid[neighbor[0]][neighbor[1]] == "1":
                    visited.add(neighbor)
                    queue.append(neighbor)


    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None or len(grid) == 0:
            return 0 

        visited = set()
        num = 0 
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    self.bfs(grid, r, c, visited)
                    num += 1
        
        return num
```
