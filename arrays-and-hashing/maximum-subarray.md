---
description: '#grind75 #neetcode150 #prefixSum #divideAndConquer'
---

# 🟡 Maximum Subarray

Given an integer array `nums`, find the subarray with the largest sum, and return _its sum_.

## Solution 1: Kadane's Algorithm

Kadane's Algorithm is similar to sliding window strategy.

{% code overflow="wrap" %}
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Brute Force: O(n^2)

        for i in range(n):
            sum = 0
            for j in range(i, n)
                sum += nums[j]
                maxSum = max(sum, maxSum)

        Solution: 
        According to Kadane's algorithm, the max subarray at index i max(nums[i], nums[i] + curr_sum@(i-1)). The second option will be chosen when maxSum[i-1] > 0.
        - curr_sum = max(nums[i], nums[i] + curr_sum)
        - maxSum = max(maxSum, curr_sum
        
        Another way of implementing this:
        - Calculate curr_sum i.e. maxSum + nums[i]
        - maxSum = max(maxSum, curr_sum)
        - If curr_sum < 0, curr_sum = 0 (effective removing negative prefix)
        
        TC: O(n)
        SC: O(1)
        '''
        maxSum = -float('inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            maxSum = max(maxSum, curr_sum)

            if curr_sum < 0: #ignoring negative prefix for next iteration 
                curr_sum = 0  

        return maxSum
```
{% endcode %}

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Solution 2: Divide and Conquer approach

{% code overflow="wrap" %}
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Divide and Conquer approach

        Max sum of given array = max(max sum of left subarray, max sum of right subarray, sum of array whose index starts in left array and ends in right array)
        
        TC: O(nlogn)
        SC: O(1)
        '''
        def util(arr):
            if len(arr) == 1:
                return arr[0]

            m = len(arr) // 2
            left_mss = util(arr[:m])
            right_mss = util(arr[m:])

            summ = 0
            left_sum, right_sum = -float('inf'), -float('inf')

            for i in range(m, len(arr)):
                summ += arr[i]
                left_sum = max(summ, left_sum)

            summ = 0
            for i in range(m-1, -1, -1):
                summ += arr[i]
                right_sum = max(right_sum, summ)

            return max(left_sum + right_sum, max(left_mss, right_mss))

        return util(nums)
```
{% endcode %}
