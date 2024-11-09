# 🟡 Rotting Oranges

You are given an `m x n` `grid` where each cell can have one of three values:

* `0` representing an empty cell,
* `1` representing a fresh orange, or
* `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a fresh orange_. If _this is impossible, return_ `-1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

<pre><code><strong>Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
</strong><strong>Output: 4
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
</strong><strong>Output: -1
</strong><strong>Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: grid = [[0,2]]
</strong><strong>Output: 0
</strong><strong>Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
</strong></code></pre>

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 10`
* `grid[i][j]` is `0`, `1`, or `2`.

```python
# https://leetcode.com/problems/rotting-oranges/description/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Solution: 
        - It is evident that this is a graph problem, but which algo should we use? 
        - We need to move to the neighbors iteratively, so BFS is the answer 
        - First count the number of fresh tomatoes at the beginning and also add the already rotton ones to the queue. You can only make the fresh oranges rotten
        - Perform BFS, and each level traversal is actually 1 timestamp
        - Check when BFS is over if there are any fresh oranges left, then return -1 

        TC: O(n)
        SC: O(n) # queue
        '''

        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        fresh = 0
        m, n = len(grid), len(grid[0])
        queue = deque()
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    queue.append((i, j))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in directions:
                    if i + dx >= 0 and i + dx < m and j + dy >= 0 and j + dy < n and grid[i+dx][j+dy] == 1:
                        grid[i+dx][j+dy] = 2 # helps avoid double counting an already rotten one as fresh
                        fresh -= 1
                        queue.append((i + dx, j + dy))

            time += 1
        
        return time if fresh == 0 else -1 

'''
2 1 1
1 1 0
0 1 1

fresh = 6
(0, 0)

(0, 1), (1, 0), fresh = 4, time=1

(0, 2), (1, 1), fresh = 2, time=2



'''
```
