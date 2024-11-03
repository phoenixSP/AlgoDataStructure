# 🟡 Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest\_common\_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T`that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

<pre><code><strong>Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
</strong><strong>Output: 3
</strong><strong>Explanation: The LCA of nodes 5 and 1 is 3.
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

<pre><code><strong>Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
</strong><strong>Output: 5
</strong><strong>Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: root = [1,2], p = 1, q = 2
</strong><strong>Output: 1
</strong></code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[2, 105]`.
* `-109 <= Node.val <= 109`
* All `Node.val` are **unique**.
* `p != q`
* `p` and `q` will exist in the tree.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        When looking for a common ancestor of two nodes in a binary tree, we can use DFS
        At each node, check if node is p or q, if p or q, return that node, if not, return None. 
        If node gets non-null value from either child and a null from the other, propagate it. When it is non-null from both side, that node is the LCA
        return that value. 
        
        Be wary that for this to work, p and q has to be distinct, otherwise, we would never a node where both child would have non-null returns
        Similarly, binary tree values have to be different
        
        TC: O(n)
        SC: O(h)
        '''

        if root is None:
            return None
        
        if root is p or root is q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if l and r: 
            return root
        
        if l is None and r is None:
            return None
        
        if l is None:
            return r
        else:
            return l
        
```
