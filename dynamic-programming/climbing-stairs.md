# 🟢 Climbing Stairs

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## Solution 1

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Solution: 
        - To reach a step n, we can go from n - 2 to n with 2-step, or n-2 to n in 2 1-steps..
        Similarly, we can go n-1 to n in 1 1-step.
        If we were to count how many differnt ways we could go to n, then we would get 
        1. Number of ways to go to n-2 (We can go two ways from n-2 to n, but the n-2 + 1-step + 1-step is covered in the n-1 option)
        + 
        2. Number of ways to go to n-1 

        i.e. count(n) = count(n-1) + count(n-2)

        TC: O(n)
        SC: O(1)
        '''
        if n <= 3:
            return n

        n1 = 2 # count of n=2
        n2 = 3 # count of n=3
        res = 0
        for i in range(4, n+1):
            res = n1 + n2
            n1 = n2
            n2 = res
        return res
```

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
