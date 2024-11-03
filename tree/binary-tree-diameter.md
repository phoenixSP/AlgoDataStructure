# 🟢 Binary Tree Diameter

Given the `root` of a binary tree, return _the length of the **diameter** of the tree_.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

<pre><code><strong>Input: root = [1,2,3,4,5]
</strong><strong>Output: 3
</strong><strong>Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: root = [1,2]
</strong><strong>Output: 1
</strong></code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-100 <= Node.val <= 100`

{% code overflow="wrap" %}
```python
# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    def __init__(self):
        self.res = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Solution: 
        - The diameter is the number of connections between two nodes (i.e. # nodes -1)
        - Diameters have a "curve point" node, which is the node that is at the highest
        - To calculate this, we would need to calculate the diameter at each node recursively
        - Traverse DFS, calculate the left subtree height, right subtree height at each node. That gives us the diameter with that particular node as the "curve point"
        - Since the output of the helper/recursive function would be the height of that subtree, we need another variable to save the diameter info, which is global in nature

        TC: O(n) # dfs traversal
        SC: O(h) # recursion stack length h is the height of the entire tree
        '''
        def getHeight(curr):
            if not curr:
                return 0 

            lh = getHeight(curr.left)
            rh = getHeight(curr.right)

            self.res = max(self.res, lh+rh)
            return 1 + max(lh, rh)

        getHeight(root)
        return self.res
```
{% endcode %}
