# 🟡 Validate Binary Search Tree

Given the `root` of a binary tree, _determine if it is a valid binary search tree (BST)_.

A **valid BST** is defined as follows:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

<pre><code><strong>Input: root = [2,1,3]
</strong><strong>Output: true
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

<pre><code><strong>Input: root = [5,1,4,null,null,3,6]
</strong><strong>Output: false
</strong><strong>Explanation: The root node's value is 5 but its right child's value is 4.
</strong></code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-231 <= Node.val <= 231 - 1`

Pay attention to example 2 where the right subtree is a BST, but the left child is not greater than the tree root, thus overall, the tree is not BST.

```python
import numpy as np
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower_limit, upper_limit):
            if root is None:
                return True

            if root.val > lower_limit and root.val < upper_limit:
                return helper(root.left, lower_limit, root.val) and helper(root.right, root.val, upper_limit)

            return False

        return helper(root, -np.inf, np.inf)
```
