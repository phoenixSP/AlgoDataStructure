# 🟡 Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

<pre class="language-python" data-overflow="wrap"><code class="lang-python"><strong># Leetcode 347 https://leetcode.com/problems/top-k-frequent-elements/description/
</strong><strong>
</strong><strong>from heapq import heappop, heappush
</strong>
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Solution: Use a length restricted minHeap to collect the biggest frequencies

        TC: O(nlogk)
        SC: O(logk)
        '''

        if nums is None or len(nums) == 0:
            return []

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        heap = []

        # use a minHeap like a maxHeap
        for num, freq in freq.items():
            heappush(heap, (freq, num))

            if len(heap) > k:
                heappop(heap)

        res = []
        while heap:
            freq, num = heappop(heap)
            res.append(num)

        return res
</code></pre>
