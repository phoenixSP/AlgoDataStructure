# Subtree of Another Tree

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot`and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

{% code overflow="wrap" %}
```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # covers the cases where either of them are none or the values are different
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Solution: 
        - Implement recursive solution for subtree 
        - Check if subroot is None, then it can be a subtree of any tree. 
        - if root is None and subroot is non-none, then return False
        - if root and subroot are same tree, return true
        - if root.left contains the subtree, or root.right contains the subtree, return true

        - m = number of nodes in root, n = number of nodes in subroot
        - TC: O(m*n) (isSame TC = O(n) worst case and isSubRoot is called m times worst case) 
        - SC:  O(logm + logn) in case of balanced trees and O(m+n) in worst case scenarios in case of unbalanced trees
        '''

        if subRoot is None: 
            return True # if subroot is None, then it is always a subtree 
        
        if root is None:
            return False # if root is None, then since subroot is not None from earlier statement, then return False
         
        if self.isSameTree(root, subRoot):
            return True 

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```
{% endcode %}
