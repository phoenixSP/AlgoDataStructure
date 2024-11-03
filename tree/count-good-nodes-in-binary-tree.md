# 🟡 Count Good Nodes In Binary Tree

Given a binary tree `root`, a node _X_ in the tree is named **good** if in the path from root to _X_ there are no nodes with a value _greater than_ X.

Return the number of **good** nodes in the binary tree.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/02/test\_sample\_1.png)

<pre><code><strong>Input: root = [3,1,4,3,null,1,5]
</strong><strong>Output: 4
</strong><strong>Explanation: Nodes in blue are good.
</strong>Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/02/test\_sample\_2.png)

<pre><code><strong>Input: root = [3,3,null,4,2]
</strong><strong>Output: 3
</strong><strong>Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: root = [1]
</strong><strong>Output: 1
</strong><strong>Explanation: Root is considered as good.
</strong></code></pre>

&#x20;

**Constraints:**

* The number of nodes in the binary tree is in the range `[1, 10^5]`.
* Each node's value is between `[-10^4, 10^4]`.

```python
class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:
        '''
        Solution: 
        - Preorder traversal is needed as we have to check if the path has any bigger values.. for that we need info about the tree's nodes 
        - Also we need to check the max value seen till now, so, always add the max(value seen till now, current root val)

        TC: O(n)
        SC: O(h)
        '''

        def helper(root, max_val):
            if root is None:
                return 0

            if root.val >= max_val:
                self.res += 1

            max_left = helper(root.left, max(max_val, root.val))
            max_right = helper(root.right, max(max_val, root.val))

        helper(root, root.val)
        return self.res
```
