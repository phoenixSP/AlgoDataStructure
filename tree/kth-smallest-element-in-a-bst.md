# 🟡 Kth Smallest Element in a BST

Given the `root` of a binary search tree, and an integer `k`, return _the_ `kth`_smallest value (**1-indexed**) of all the values of the nodes in the tree_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

<pre><code><strong>Input: root = [3,1,4,null,2], k = 1
</strong><strong>Output: 1
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

<pre><code><strong>Input: root = [5,3,6,2,4,null,null,1], k = 3
</strong><strong>Output: 3
</strong></code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is `n`.
* `1 <= k <= n <= 104`
* `0 <= Node.val <= 104`

&#x20;

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## Thought process

BST is sorted, so if we were to get the inorder traversal of the tree, then the kth element would be the kth smallest element in BST.

So if we get the complete inorder traversal list, the TC would be O(n)

If we do it iteratively, once the length of the traversal is k, we can end the loop.

check if there's at least k elements in the tree..

But this does not reduce the time complexity (technically yes, but not always. For eg, we always have to iterate till the end of the left leaf.. so if k is very small, it does not mean we only traverse k times). TC still O(n)

## Solution

<pre class="language-python"><code class="lang-python"><strong># unrestricted inorder traversal
</strong><strong>class Solution:
</strong>    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Perform DFS
        Return k-1th element (because k starts with 1)
        
        TC: O(n)
        SC: O(n)
        '''
        
        def helper(root, dfs=None):
            if root is None:
                return

            if root.left:
                helper(root.left, dfs)
            
            dfs.append(root.val)

            if root.right:
                helper(root.right, dfs)

        dfs = []
        helper(root, dfs)
        return dfs[k-1]
</code></pre>

Let's optimize the SC.. TC would technically remain the same, but would be slightly optimized

