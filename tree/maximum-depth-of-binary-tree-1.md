# 🟢 Maximum Depth of Binary Tree

Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

<pre><code><strong>Input: root = [3,9,20,null,null,15,7]
</strong><strong>Output: 3
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: root = [1,null,2]
</strong><strong>Output: 2
</strong></code></pre>

**Constraints:**

* The number of nodes in the tree is in the range `[0, 104]`.
* `-100 <= Node.val <= 100`

```python
# Leetcode 104: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    '''
    Solution: Use a stack to perform DFS iteratively (preorder)
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
