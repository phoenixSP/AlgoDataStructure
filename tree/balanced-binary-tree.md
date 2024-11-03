# 🟢 Balanced Binary Tree

Given a binary tree, determine if it is **height-balanced**.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance\_1.jpg)

<pre><code><strong>Input: root = [3,9,20,null,null,15,7]
</strong><strong>Output: true
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance\_2.jpg)

<pre><code><strong>Input: root = [1,2,2,3,3,null,null,4,4]
</strong><strong>Output: false
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: root = []
</strong><strong>Output: true
</strong></code></pre>

**Constraints:**

* The number of nodes in the tree is in the range `[0, 5000]`.
* `-104 <= Node.val <= 104`

{% code overflow="wrap" %}
```python
class Solution:
    def getHeight(self, root):
        if root is None:
            return 0 

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Solution: recursive solution using getHeight util and isBalanced 

        TC: O(n*n) =  O(n2)
        SC: O(logn + logn) = O(logn) # height of tree
        '''
        
        if root is None:
            return True

        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
```
{% endcode %}

Optimized solution of O(n)

```python
class Solution:
    def getHeight(self, root, balanced=None):
        if root is None:
            return 0 

        left_height = self.getHeight(root.left, balanced)
        right_height = self.getHeight(root.right, balanced)

        if abs(left_height - right_height) > 1:
            balanced[0] = False

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Solution: recursive solution using getHeight util and isBalanced 

        TC: O(n*n) =  O(n)
        SC: O(logn) = O(logn) # height of tree
        '''
        
        if root is None:
            return True

        balanced = [True]
        self.getHeight(root, balanced)
        return balanced[0]
```
