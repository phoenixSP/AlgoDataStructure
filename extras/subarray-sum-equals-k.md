---
description: '#prefixSum #array'
---

# 🟡 Subarray sum equals k

Given an array of integers `nums` and an integer `k`, return _the total number of subarrays whose sum equals to_ `k`. A subarray is a contiguous **non-empty** sequence of elements within an array.

{% code overflow="wrap" %}
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Brute force solution would be to loop over all the subarrays to get their sum and check if it is equal to k
        There would be two nested for loops. for i in range(n): for j in range(i, n)
        TC: O(n^2)
        SC: O(1)

        Solution: 
        sum of subarray (i, j) = sum of subarray(0, j) - sum of subarray(0, i)
        We can keep a track of the sum of subarray (0, i) or rather count of the unique sums. This is because the presence of negative numbers can cause multiple subarrays have the same sum
        Use prefix sum hashmap to track sum of different prefixes and their count
        TC: O(n)
        SC: O(1)
        '''

        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1 and nums[0] == k:
            return 1

        count = 0
        current_sum = 0
        prefix_sum = {0: 1} # signifies base condition of empty subarray having the sum of 0

        for i in range(len(nums)):
            current_sum += nums[i]

            difference = current_sum - k
            count += prefix_sum.get(difference, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count
```
{% endcode %}
