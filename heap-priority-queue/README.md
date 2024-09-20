# 💯 Heap/Priority Queue

A heap is a specialized tree-based data structure which is a complete tree that satisfies the heap property.

* Max heap - In a max heap, the value of a node must be greatest among the node values in its entire subtree. The same property must be recursively true for all nodes in the tree.
* Min heap - In a min heap, the value of a node must be smallest among the node values in its entire subtree. The same property must be recursively true for all nodes in the tree.

#### Time Complexity

<table><thead><tr><th width="519">Operation</th><th width="228">Big-O	</th></tr></thead><tbody><tr><td>Find min/max</td><td>O(1)</td></tr><tr><td>Insertion</td><td>O(log(n))</td></tr><tr><td>Remove</td><td>O(log(n))</td></tr><tr><td>Heapify (create a heap out of given array of elements)</td><td>O(n)</td></tr></tbody></table>

#### Techniques

* Mention of k : If the question mentions top or lowest k items, then heap can be used.&#x20;

If you require the top _k_ elements use a Min Heap of size _k_. Iterate through each element, pushing it into the heap (for python `heapq`, invert the value before pushing to find the max). Whenever the heap size exceeds _k_, remove the minimum element, that will guarantee that you have the _k_ largest elements.
