# 🟡 Maximum Product Subarray

Given an integer array `nums`, find a&#x20;

subarray that has the largest product, and return _the product_.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Example 1:**

<pre><code><strong>Input: nums = [2,3,-2,4]
</strong><strong>Output: 6
</strong><strong>Explanation: [2,3] has the largest product 6.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [-2,0,-1]
</strong><strong>Output: 0
</strong><strong>Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
</strong></code></pre>

**Constraints:**

* `1 <= nums.length <= 2 * 104`
* `-10 <= nums[i] <= 10`
* The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit**integer.

The solution draws inspiration from Kadane's algo

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        - it is an integer array, so no fractions possible
        - subarray is a contiguous non empty sequence
        
        Solution: 
        - Keep track of both the minimum and maximum products of the subarrays because if we have a negative number at i, we can use both the values to check which value is bigger
        
        TC: O(n)
        SC: O(1)
        '''

        if not nums or len(nums) == 0:
            return 1
        
        max_prod = nums[0] # if there's only one value
        curr_max, curr_min = 1, 1 #tracking the min and max till now

        for num in nums:
            temp = curr_max*num 
            # comparing num as well because sometimes if both the curr_min and curr_max is positive, and num is negative, then num alone would be the max number. all other combinations will be smaller
            curr_max = max(temp, curr_min*num, num) # using previous curr_min and curr_max values
            curr_min = min(temp, curr_min*num, num)
            max_prod = max(curr_max, max_prod)

            # in the situation num = 0, curr_min and curr_max both would become 0
            # when we go to the next num, then we have to ignore the previous subarray because it has a zero, which can be achieved by having num in the min and max functions
        
        return max_prod
```
