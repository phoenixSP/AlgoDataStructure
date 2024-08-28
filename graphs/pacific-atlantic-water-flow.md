# 🟡 Pacific Atlantic Water Flow

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return _a **2D list** of grid coordinates_ `result` _where_ `result[i] = [ri, ci]` _denotes that rain water can flow from cell_ `(ri, ci)` _to **both** the Pacific and Atlantic oceans_.

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    '''
    TC: O(number of nodes) = O(m*n) where m,n = dims of heights
    '''

        nrows, ncols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            
            if (r < 0 or c < 0 or r >= nrows or c >= ncols or (r,c) in visited or heights[r][c] < prev_height):
                # since we are moving from sea to land, hence prev_height has to be equal or greater than current
                return 

            visited.add((r,c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for row in range(nrows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, ncols-1, atlantic, heights[row][ncols-1])

        for col in range(ncols):
            dfs(0, col, pacific, heights[0][col])
            dfs(nrows-1, col, atlantic, heights[nrows-1][col])

        res = []
        for row in range(nrows):
            for col in range(ncols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append((row, col))
        
        return res
```
