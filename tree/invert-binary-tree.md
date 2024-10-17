# 🟢 Invert Binary Tree

Given the `root` of a binary tree, invert the tree, and return _its root_.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-09-22 at 7.50.47 AM.png" alt="" width="375"><figcaption></figcaption></figure>

{% code overflow="wrap" %}
```python
# Leetcode 226: https://leetcode.com/problems/invert-binary-tree/description/

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Solution: 
        Use recursion to inverse the subtrees

        TC: O(n)
        SC: O(h) # height of tree
        '''
        if root is None:
            return root

        # invert each subtree and assign to opposite parents
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```
{% endcode %}
