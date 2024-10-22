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
            row, col = queue.popleft() # O(1)
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

DFS alternative without visited

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        count the number of connected components

        '''
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):

            # check if the conditions are valid:
            if i < 0 or j < 0 or i >= n_rows or j >= n_cols or grid[i][j] == "0":
                return 

            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
            return
        
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
```
