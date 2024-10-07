# Same Tree

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

{% code overflow="wrap" %}
```python
# Leetcode 100: https://leetcode.com/problems/same-tree/description/

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        TC: O(min(m, n)) where m and n are the number of nodes in the trees. Since we only visit each node once, it's linear
        SC: O(h) where h is the height of the tree. The recursive stack is of h size. In worst case, h is n in case of a skewed tree, in best case logn (balanced tree)
        '''
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # covers the cases where either of them are none or the values are different
            return False
```
{% endcode %}
