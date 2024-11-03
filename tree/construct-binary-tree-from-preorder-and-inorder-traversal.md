# 🟡 Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return _the binary tree_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

<pre><code><strong>Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
</strong><strong>Output: [3,9,20,null,null,15,7]
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: preorder = [-1], inorder = [-1]
</strong><strong>Output: [-1]
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= preorder.length <= 3000`
* `inorder.length == preorder.length`
* `-3000 <= preorder[i], inorder[i] <= 3000`
* `preorder` and `inorder` consist of **unique** values.
* Each value of `inorder` also appears in `preorder`.
* `preorder` is **guaranteed** to be the preorder traversal of the tree.
* `inorder` is **guaranteed** to be the inorder traversal of the tree.

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Solution
        - Preorder has root, left tree and right tree and inorder has left tree, root, right tree
        - So, root in preorder would be at 0 index. Using the value of root, search for middle of tree, i.e. root in the inorder traversal
        - This would mean that the tree has to have unique values.. 
        - the index of root in inorder would divide the list into the left subtree and right subtree
        - Recursively call build tree on the two sublists 
        
        TC: O(n^2) because checking index of the root is O(n) and DFS is O(n)
        SC: O(n^2) -> O(n^2) because of the repeated slicing operations and O(n) for the recursion depth.
        '''

        if not preorder and not inorder:
            return 

        val = preorder[0]
        mid = inorder.index(val)

        root = TreeNode(val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
```

Optimizing the two pain points of above algo&#x20;

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Solution
        Optimising two parts, index and slicing
        
        TC: O(n) because DFS is O(n)
        SC: O(n) O(n) for the recursion depth and O(n) for the dictionary
        '''
        hashmap = {val:idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def helper(l, r):
            if l > r: 
                return None

            val = preorder[self.pre_idx]
            mid = hashmap[val]

            root = TreeNode(val)
            self.pre_idx += 1
            
            root.left = helper(l, mid-1)
            root.right = helper(mid+1, r)

            return root

        return helper(0, len(inorder)-1)
```
