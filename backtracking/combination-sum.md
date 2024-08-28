# 🟡 Combination sum

Given an array of **distinct** integers `candidates` and a target integer `target`, return _a list of all **unique combinations** of_ `candidates` _where the chosen numbers sum to_ `target`_._ You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the&#x20;

frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

## Solution

{% code overflow="wrap" %}
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Solution: 
        - We can view it as a decision tree where we add a number at each step

                                    Null 
                    [2]     [3]     [6]     [7]
        [2,2][2,3][2,6][2,7] [3,2][3,3][3,6][3,7] [6,2][6,3][6,6][6,7] [7,2][7,3][7,6][7,7]
        and so on. 

        When the node sum > target, we don't compute it's children anymore. 

        But the problem is that we would get duplicate nodes with this process: [2,2,3] and [3,2,2]. 

        Hence we have to modify the solution: 
        - For each index we have to decide whether to include an element or to exclude it. 

                                    Null
                            [2]                                         []
        [2,2]                               [2]                         [3]     []
        [2,2,2]             [2,2]             [2,3] [2]                 [3,3] [3]   [6]
        [2,2,2,2][2,2,2]    [2,2,3] [2,2]      [2,3,3] [2,2] [2,6] [2]  [3,3,3] [3,3] [3,6] [3] [6,6] [6]

        and so on. 

        Algorithmically, we can taking creating two options at every step, to include current index or not.
        
        TC: Recursion decision tree with two choices at each node. The max depth of the tree is going to be t because all the numbers in the array are positive, and we have to get the depth enough to make total = target. Hence, it is 2^Target.
        '''

        if target < 2:
            return []
        
        res = [] # no set required because the algorithm would not produce permutations
        
        def dfs(i, curr, total):
            if target == total:
                # combination is equal to curr
                res.append(curr.copy()) # we have to have a copy because otherwise it would save the reference and curr would be modified
                return 

            if i >= len(candidates) or total > target:
                return 

            # first choice 
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            # second choice 
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)

        return res
```
{% endcode %}
