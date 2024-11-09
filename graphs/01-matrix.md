# 🟡 01 Matrix

Given an `m x n` binary matrix `mat`, return _the distance of the nearest_ `0` _for each cell_.

The distance between two adjacent cells is `1`.

{% code overflow="wrap" %}
```python
from collections import deque
import numpy as np

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        Solution: 
        - Perform BFS on all the positions and check if all of them are visited
        - if the position is a 0, then their distance is 0
        - if an position is a 1 and has 0 in its neighborhood, then the distance is 1
        - if the position is a 1 with no 0 in its neighborhood, then its distance is min(all neighbor's distance) + 1

        TC: DFS O(m*n)
        SC: O(m*n)
        
        Note: Implicit Visit Tracking is done when the distance is updated from inf to standard number, thats why visited set is not needed
        '''

        # base condition 
        if mat is None or len(mat) == 0:
            return mat

        n_rows, n_cols = len(mat), len(mat[0])
        output = [[np.inf] * n_cols for _ in range(n_rows)] # make sure its not shallow
        
        queue = deque()
        # add all positions with 0 in the queue
        for i in range(n_rows):
            for j in range(n_cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    output[i][j] = 0  # setting distance = 0 for 0 positions
        print(queue)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n_rows and 0 <= ny < n_cols and output[nx][ny] > output[x][y] + 1:
                    output[nx][ny] = output[x][y] + 1 # value is updated when the lowest neighbor comes
                    queue.append((nx, ny))

        return output
```
{% endcode %}
