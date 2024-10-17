# 🟡 Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest\_common\_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Constraints:**

* The number of nodes in the tree is in the range `[2, 105]`.
* `-109 <= Node.val <= 109`
* All `Node.val` are **unique**.
* `p != q`
* `p` and `q` will exist in the BST.

### Iterative solution

{% code overflow="wrap" %}
```python
# Leetcode 235: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        - Start looking from the root. If p and q are on the same side, curr = root.<side>
        - Keep looking till q and p are on opposite sides or equal to curr
        - When in opposite sides or one node = curr, curr is the LCA
        TC: O(h) where h is height of tree. At each level, this algo only visits one node
        h = logn for balanced tree
        '''
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # covers the cases where either node is equal to the curr val
                # or p and q lies on the opposite sides, which means curr is the LCA
                return curr
        
        # since problem is guarenteed to have p, q, we don't need to return anything
        # We also don't need to check if the nodes actually exist or not. Once we find the lowest ancestor, we know that the two nodes exist in the subtree
        
```
{% endcode %}

### Recursive Solution

{% code overflow="wrap" %}
```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        - Start looking from the root. If p and q are on the same side, curr = root.<side>
        - Keep looking till q and p are on opposite sides or equal to curr
        - When in opposite sides or one node = curr, curr is the LCA
        TC: O(h) where h is height of tree. At each level, this algo only visits one node
        h = logn for balanced tree
        '''
        # since problem is guarenteed to have p, q, we don't need to check for root is None condition as it will never go to the leaf nodes
        # unless only checking for base condition
        if root is None:
            return None
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
            # covers the cases where either node is equal to the curr val
            # or p and q lies on the opposite sides, which means curr is the LCA        
    
```
{% endcode %}
