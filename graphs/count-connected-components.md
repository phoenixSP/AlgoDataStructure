# 🟡 Count connected components

There is an undirected graph with `n` nodes. There is also an `edges` array, where `edges[i] = [a, b]` means that there is an edge between node `a` and node `b` in the graph.

Return the total number of connected components in that graph.

## Solution I

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        TC: O(E+V) 
        '''
        if n == 1:
            return 1

        visited = set()

        adj_list = {i: [] for i in range(n)}

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            if node in visited:
                return 

            visited.add(node)

            for neighbor in adj_list[node]:
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
```

## Solution II

Union find can also be used for this problem.&#x20;
