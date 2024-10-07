# Maximum Depth of Binary Tree

Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

First we look at the recursive solution.

{% code overflow="wrap" %}
```python
class Solution:
    '''
    Solution:
    - recursive solution
    - maxDepth at node = 1 + max(depth of left subtree, depth of right subtree)
    TC: O(n) because it has to go to all nodes
    SC: O(h) where h=height of tree (for recursion stack)
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
        return max_depth

```
{% endcode %}

The next solution uses iterative BFS to solve the problem. This has no algorithmic advantage.&#x20;

{% code overflow="wrap" %}
```python
from collections import deque

class Solution:
    '''
    Solution: Use a queue to perform BFS iteratively
    TC: O(n) where n is number of nodes
    SC: O(h) where h is height of tree
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            depth +=1
            for _ in range(len(queue)): # this calculates the length of the queue at the beginning
                node = queue.popleft()
                # add the left and right children of node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                    
        return depth
```
{% endcode %}

Iterative DFS solution (Preorder)

{% code overflow="wrap" %}
```python
class Solution:
    '''
    Solution: Use a queue to perform DFS iteratively (preorder)
    TC: O(n) where n is number of nodes
    SC: O(h) where h is height of tree
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)

            if node.left:
                stack.append([node.left, depth+1])

            if node.right:
                stack.append([node.right, depth+1])

        return res
```
{% endcode %}
