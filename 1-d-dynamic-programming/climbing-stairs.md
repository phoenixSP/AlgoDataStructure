# 🟢 Climbing Stairs

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## Solution 1



## Solution 2

Here's a DFS solution that uses backtracking (not optimal)

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(curr, total):
            if total == n:
                res.append(curr.copy())
                return 
            
            if total > n:
                return

            curr.append(1)
            dfs(curr, total + 1)
            curr.pop()
            curr.append(2)
            dfs(curr, total+2)
            curr.pop()

        res = []
        dfs([], 0)
        print(res)

        return len(res)
```
