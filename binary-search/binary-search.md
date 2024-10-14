# 🟢 Binary Search

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

&#x20;

**Example 1:**

<pre><code><strong>Input: nums = [-1,0,3,5,9,12], target = 9
</strong><strong>Output: 4
</strong><strong>Explanation: 9 exists in nums and its index is 4
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [-1,0,3,5,9,12], target = 2
</strong><strong>Output: -1
</strong><strong>Explanation: 2 does not exist in nums so return -1
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-104 < nums[i], target < 104`
* All the integers in `nums` are **unique**.
* `nums` is sorted in ascending order.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        - Define left and right for left end and right end of array
        - Mid = (left + right)/2
        - Check if mid is target, else check if target > mid: left = mid + 1,
        else if target < mid: right = mid -1

        TC: O(logn) because each time the array is divided into 2 parts and only one is chosen. that means 2^x=n where x is the number of times the array is divided
        '''

        if nums is None or len(nums) == 0:
            return -1

        left, right = 0, len(nums)-1

        while left <= right:
            mid = int((left + right)/2)

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```
