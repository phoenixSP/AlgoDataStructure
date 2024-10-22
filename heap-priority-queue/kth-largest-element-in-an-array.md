# 🟡 Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return _the_ `kth` _largest element in the array_.

Note that it is the `kth` largest element in the sorted order, not the `kth`distinct element.

Can you solve it without sorting?

&#x20;

**Example 1:**

<pre><code><strong>Input: nums = [3,2,1,5,6,4], k = 2
</strong><strong>Output: 5
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
</strong><strong>Output: 4
</strong></code></pre>

{% code overflow="wrap" %}
```python
from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return None
        minHeap = nums[:k]
        heapify(minHeap)
        
        for num in nums[k:]:
            if num > minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, num)

        return minHeap[0]
```
{% endcode %}
