# 🟡 K Closest Points to Origin

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `√(x1 - x2)2 + (y1 - y2)2`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

{% code overflow="wrap" %}
```python
# leetcode 973: https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import heappush, heappop
import numpy as np

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Solution: 

        - Calculate all the distances individually and then push the distances in a minHeap
        - Restrict the minHeap size to k and use heappop followed by push to keep the length constant
        - Multiply the distance with a negative to pop out bigger numbers 

        TC: O(k) [initial heap] + O((n-k)logk) == O(nlogk)
        SC: O(k)
        '''

        if points is None or len(points) == 0:
            return []

        heap = []

        for i, pt in enumerate(points):
            distance = np.sqrt(pt[0]**2 + pt[1]**2)
            heappush(heap, (-distance, i, pt))

            if len(heap) > k:
                # first push the new pt, then pop the extra one
                heappop(heap)

        res = []
        while heap:
            _, _, pt = heappop(heap)
            res.append(pt)

        return res
```
{% endcode %}
