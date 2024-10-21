# 🟡 House Robber

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has. The houses are arranged in a straight line, i.e. the `i`th house is the neighbor of the `(i-1)`th and `(i+1)`th house.

You are planning to rob money from the houses, but you cannot rob **two adjacent houses** because the security system will automatically alert the police if two adjacent houses were _both_broken into.

Return the _maximum_ amount of money you can rob **without** alerting the police.

{% code overflow="wrap" %}
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        This is the reverse order relationship.
        rob = max(arr[0] + rob(arr[2:]), arr[1] + rob(arr[3:])) # recurrence relationship

        While coding, the reverse relationship can be a little confusing, so we can write the relationship from left to right
        - At any house, we can choose to ignore that house, ie take max till housei-1, or take max till housei-2 + curr house

        Solution
        - This is a DP problem
        - Initialize two params rob1 and rob2 signifying housei-2 and housei-1
        - Iterate over the array, at any housei the max loot would be max(housei-1, housei-2 + housei)
        
        TC: O(n)
        SC: O(1)
        '''

        if nums is None:
            return 0 
        
        rob1 = 0
        rob2 = 0
        res = 0

        for num in nums:
            res = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = res
        return res
```
{% endcode %}
