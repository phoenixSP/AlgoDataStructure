# 💯 Tree

* Hierachical abstract data structure with a set of connected nodes
* Each node can be connected to many children, but a child must have only one parent. The root node is the exception to this rule, which has no parent
* Trees are undirected and connected acycitc graphs with no cycles or loops
* They are commonly used to represent hierarchical data, eg. file systems, JSON, HTML.
* Important terminology
  * **Degree: Number of children of a node**
  * **Degree of a tree:** Maximum degree of nodes in the tree
  * **Depth** - Number of edges along the unique path between a node and the root node
  * **Width** - Number of nodes in a level

## Binary Trees

* Each node has a maximum of two childresn
* A complete binary tree has two children on each level except the last, and the nodes in the last level are as far left as possible. Usage example: Heaps where the complete property helps in keeping operations like insertion, deletion O(log n)&#x20;
* A balanced tree is a binary tree where the height of the left and right subtree of each node differs by 1 at most. Balanced or self balanced trees are frequently used in database indexing (AVL, B-Tree etc)

### Tree traversal

<figure><img src="../.gitbook/assets/Screenshot 2024-09-21 at 6.46.52 PM.png" alt="" width="375"><figcaption><p>Source: <a href="https://www.techinterviewhandbook.org/algorithms/tree/">Link</a></p></figcaption></figure>

There are two fundamental traversal algorithms: Depth First Search and Breadth First Search.&#x20;

| Aspect                | BFS                                  | DFS                                              |
| --------------------- | ------------------------------------ | ------------------------------------------------ |
| **Traversal Method**  | Explores level by level (breadth)    | Explores depth first, diving into branches       |
| **Data Structure**    | Queue                                | Stack (or recursion)                             |
| **Traversal Variant** | Level Order                          | Pre-order, in-order, post-order                  |
| **Typical Use Cases** | Level-order traversal, shortest path | Tree traversal for copying, sorting, or deleting |
| **Time complexity**   | O(n)                                 | O(n)                                             |

### DFS

<details>

<summary>Algorithm example (iterative preorder DFS for max depth of tree</summary>

{% code overflow="wrap" %}
```python
class Solution:
    '''
    Solution: Use a queue to perform DFS iteratively (preorder)
    TC: O(n) where n is number of nodes
    SC: O(h) where h is height of tree
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)

            if node.left:
                stack.append([node.left, depth+1])

            if node.right:
                stack.append([node.right, depth+1])

        return res
```
{% endcode %}

</details>

### BFS

<details>

<summary>Algorithm</summary>

The following is a basic algorithm for level order traversal.

{% code overflow="wrap" %}
```python
from collections import deque

class Solution:
    '''
    Solution: Use a queue to perform BFS iteratively
    TC: O(n) where n is number of nodes
    SC: O(h) where h is height of tree
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = []
            for _ in range(len(queue)): # this calculates the length of the queue at the beginning
                node = queue.popleft()
                level.append(node.val)
                # add the left and right children of node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
                    
        return res
```
{% endcode %}

</details>

### In-order traversal

Inorder traversal pattern is Left -> Root -> Right. Hence, the inorder traversal of the given tree is \[2, 7, 5, 6, 11, 1, 9, 5, 9]

### Pre-order traversal

Preorder transversal pattern is Root -> Left -> Right. The preorder traversal of the given tree is \[1, 7, 2, 6, 5, 11, 9, 9, 5].

### Post order traversal

Post order transversal pattern is Left -> Right -> Root. The preorder traversal of the given tree is \[2, 5, 11, 6, 7, 5, 9, 9, 1].&#x20;

In-order traversal of a binary tree alone is insufficient to uniquely serialize a tree. Pre-order or post-order traversal is also required.

### Level order traversal

In level order, we use BFS to traverse each level of tree first before going to the next. Here the the level order traversal of the binary tree is \[1, 7, 9, 2, 6, 9, 5, 11, 5].

## Binary Search Tree (BST)

* Binary search trees are binary trees with a specific property: the left child value <=  parent value, and the right node value >= parent value
* They are used for fast search, insertion, and deletion operations
* We can traverse a BST same as a tree i.e. pre-order, in-order, post-order and level order. The first three are depth first searches, while level order is a breadth first search
* The inorder traversal of a BST is sorted

| Operation | Time complexity Big O |
| --------- | --------------------- |
| Access    | O(log n)              |
| Search    | O(log n)              |
| Insert    | O(log n)              |
| Delete    | O(log n)              |

Great resource: [https://samuelalbanie.com/files/digest-slides/2022-10-brief-guide-to-binary-search-trees.pdf](https://samuelalbanie.com/files/digest-slides/2022-10-brief-guide-to-binary-search-trees.pdf)

## Practical know-how

#### Corner cases

* Empty tree
* Single node
* Two nodes
* Very skewed tree (like a linked list)

#### Techniques

* Recursion
* Traversal by level
* Summation of nodes (nodes can be negative)

## Advanced Topics

## Self-Balancing Binary Search Tree/Red Black Tree

* Cheatsheet: [https://samuelalbanie.com/files/digest-slides/2022-12-brief-guide-to-red-black-trees.pdf](https://samuelalbanie.com/files/digest-slides/2022-12-brief-guide-to-red-black-trees.pdf)
* Video resource: [https://www.youtube.com/watch?v=q4fnJZr8ztY](https://www.youtube.com/watch?v=q4fnJZr8ztY)

### B-Tree

* Cheatsheet: [https://samuelalbanie.com/files/digest-slides/2022-12-brief-guide-to-b-trees.pdf](https://samuelalbanie.com/files/digest-slides/2022-12-brief-guide-to-b-trees.pdf)

### AVL Tree

* Resources: [https://www.techinterviewhandbook.org/algorithms/tree/](https://www.techinterviewhandbook.org/algorithms/tree/)
