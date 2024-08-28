# 🟡 Valid Tree

Given `n` nodes labeled from `0` to `n - 1` and a list of **undirected** edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

**Note:**

* You can assume that no duplicate edges will appear in edges. Since all edges are `undirected`, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.

**Constraints:**

* `1 <= n <= 100`
* `0 <= edges.length <= n * (n - 1) / 2`

{% code overflow="wrap" %}
```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        A tree is a graph with no loops and is connected
        Empty graph is also considered a tree
        '''

        def dfs(node, prev):

            if node in visited: 
                return False # presence of loop

            visited.add(node)
            for neighbor in adj_dict[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True

        if not n:
            return True
        
        visited = set()
        adj_dict = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adj_dict[n1].append(n2)
            adj_dict[n2].append(n1)
        
        return dfs(0,-1) and n == len(visited)
```
{% endcode %}
