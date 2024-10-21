# 🟢 Two Sum

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have _**exactly**_** one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

{% code overflow="wrap" %}
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute force solution: 
        compare each pair combination for their sum. Do this using nested loop. i iterates over the entire length, and j iterates from i+1 to end of array

        Another solution: Sort the array, and have two pointers from each end for the search. This has TC O(nlogn) and SC O(1)

        Solution:
        - Create a hashmap to same the array value in dict key and array index in dict value
        - if difference between current item and target exists in hashmap, return the indices
        TC: O(n) (only one iteration)
        SC: O(n) (space for hashmap)
        '''

        hashmap = {}

        for i, num in enumerate(nums):
            if target - num in hashmap:
                return i, hashmap[target-num]
            hashmap[num] = i
        
        # problem guarentees that a solution exists, so no need to return anything
        return
```
{% endcode %}
