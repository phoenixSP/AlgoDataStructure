# 🟡 House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

```python
class Solution:
    def rob_util(self, nums):
        if not nums:
            return 0

        rob1, rob2, res = 0, 0, 0
        for num in nums:
            res = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = res
        return res

    def rob(self, nums: List[int]) -> int:
        '''
        Solution: 
        - The houses are arranged in a circle, so we have to consider the house_1 when looking at house_n
        - The way to do it is to calculate rob on nums[0:n-1] (remove last house) or nums[1:] (remove first house)
        - At any house, we can choose to ignore that house, ie take max till housei-1, or take max till housei-2 + curr house

        Solution: 
        - Call the following function on the two subarrays
        - Initialize two params rob1 and rob2 signifying housei-2 and housei-1
        - Iterate over the array, at any housei the max loot would be max(housei-1, housei-2 + housei)
        - Return the max of the two

        TC: O(n)
        SC: O(1)
        '''

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        return max(self.rob_util(nums[:n-1]), self.rob_util(nums[1:]))
```
