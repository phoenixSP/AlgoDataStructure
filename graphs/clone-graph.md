# 🟡 Clone Graph

Given a reference of a node in a [**connected**](https://en.wikipedia.org/wiki/Connectivity\_\(graph\_theory\)#Connected\_graph) undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object\_copying#Deep\_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

## &#x20;Solution

```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        SOlution: 
        - Create a hashmap to keep track of the copies of each node 
        TC: O(n)
        '''

        old_to_new = {}

        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            old_to_new[node] = Node(node.val)

            for neighbor in node.neighbors:
                old_to_new[node].neighbors.append(clone(neighbor))
            
            return old_to_new[node]

        return clone(node) if node else None
```
