# 🟡 Binary tree right side view

Given the `root` of a binary tree, imagine yourself standing on the **right side**of it, return _the values of the nodes you can see ordered from top to bottom_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

<pre><code><strong>Input: root = [1,2,3,null,5,null,4]
</strong><strong>Output: [1,3,4]
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: root = [1,null,3]
</strong><strong>Output: [1,3]
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: root = []
</strong><strong>Output: []
</strong></code></pre>

```python
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Solution: 
        - Level order the tree and only save the nodes at the end

        TC: O(n)
        SC: O(n) for queue use
        '''

        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n_level = len(queue)
            for i in range(n_level):
                node = queue.popleft()
                if i == n_level -1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return res
```
