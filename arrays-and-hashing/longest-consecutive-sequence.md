---
description: '#hashmap'
---

# 🟡 Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return _the length of the longest consecutive elements sequence._

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

<pre><code><strong>Input: nums = [100,4,200,1,3,2]
</strong><strong>Output: 4
</strong><strong>Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [0,3,7,2,5,8,4,6,0,1]
</strong><strong>Output: 9
</strong></code></pre>

**Constraints:**

* `0 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`

{% code overflow="wrap" %}
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Brute force:
        Sort and count contiguous string
        TC: O(nlogn) for sorting
        
        Solution:
        Since the question asks for a O(n) solution, we create a hashset to retrieve in O(1) time. 
        Each "sequence" of numbers can be thought of a set, the first number does not have num-1 in the list. Each number that follows adds to the length.
        TC: O(n)
        SC: O(n)
        '''
        
        if nums is None or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        hashset = set(nums) 
        max_length = -1
        for num in nums:
            # check if this is start of sequence
            if num-1 not in hashset: # average TC of search in set = O(1)
                length = 0
                while num + length in hashset:
                    length += 1
                
                max_length = max(max_length, length)
                
        return max_length
```
{% endcode %}
