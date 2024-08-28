---
description: '# PrefixSum'
---

# 🟡 Product of Array Except Self

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## Solution

Product of all elements would cause issues when there's a zero.

{% code overflow="wrap" %}
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return nums
        
        if len(nums) == 1:
            return [1]

        left_prefix_mul = [1]*len(nums)
        right_prefix_mul = [1]*len(nums)
        output = [1]*len(nums)


        for i in range(1, len(nums)):
            left_prefix_mul[i] = left_prefix_mul[i-1]*nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            right_prefix_mul[j] = right_prefix_mul[j+1]*nums[j+1]
        

        for k in range(len(nums)):
            output[k] = left_prefix_mul[k]*right_prefix_mul[k]

        return output
```
{% endcode %}

We can further optimize this by using less arrays, and as output array memory does not count, so we reduce our space complexity to O(1).

{% code overflow="wrap" %}
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return nums
        
        if len(nums) == 1:
            return [1]

        output = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        print(output)

        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        return output
```
{% endcode %}
