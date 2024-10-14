# 🟡 Search in Rotated Sorted Array

There is an integer array `nums` sorted in ascending order (with **distinct**values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of_ `target` _if it is in_ `nums`_, or_ `-1` _if it is not in_ `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

&#x20;

**Example 1:**

<pre><code><strong>Input: nums = [4,5,6,7,0,1,2], target = 0
</strong><strong>Output: 4
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [4,5,6,7,0,1,2], target = 3
</strong><strong>Output: -1
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: nums = [1], target = 0
</strong><strong>Output: -1
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 5000`
* `-104 <= nums[i] <= 104`
* All values of `nums` are **unique**.
* `nums` is an ascending array that is possibly rotated.
* `-104 <= target <= 104`

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        - Look at the problem from a two array pov: a left array and a right array
        - The left and right array are both increasing in nature, and the max element 
        in right array is lesser than the left array min element
        - If target is in left array, check if it is greater than mid. If target is greater, then 
        target should be to the right of mid. If target is smaller than mid, it can be either in the left of mid, 
        or in the right array. 
        - Cases can be condensed together
        TC: O(logn) as the array is repeatedly divided into two and each half is discarded
        SC: O(1)
        '''

        left, right = 0, len(nums) - 1

        while left <= right: 
            # equal covering the case where the array just has one element

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # mid in left array case
                # equal covering single element case

                # if target > nums[mid]:
                #     # look to right of mid
                #     left = mid + 1
                # elif target < nums[mid]:
                #     if target >= nums[left]:
                #         right = mid -1
                #     elif target < nums[left]:
                #         left = mid + 1

                # merge above cases together
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    # target is smaller than mid but larger equal to left
                    right = mid - 1

            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    # target is greater than mid but smaller equal to right
                    left = mid + 1

        return -1
```
