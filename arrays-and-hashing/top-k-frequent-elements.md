# 🟡 Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

{% code overflow="wrap" %}
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Solution 1; Implemented below using bucket sort
        - Calculate the frequency map of the nums array
        - Pivot the map into a frequency array where the indices signify the frequency
        - Iterate over the frequency array and get top k elements (iterate over subarrays)
        TC: O(n)
        SC: O(n)
        
        Solution 2:
        Create count hashmap, create maxheap, and pop k times
        TC: O(n), SC: O(n)
        '''
        counter = {}
        frequency_arr = [[] for i in range(len(nums)+1)] # 0 = 0 frequency; max frequency possiblem is len(nums)

        # create count hashmap; TC: O(n)
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for val, count in counter.items():
            frequency_arr[count].append(val)

        # O(n)
        res = []
        for i in range(len(frequency_arr)-1, 0, -1):
            for n in frequency_arr[i]:
                res.append(n)

                if len(res) == k: # we are guarenteed a result, and a unique one as well. That means if unique numbers a and b have same counts, and are expected to be in the answer, k will include both of them
                    return res

        return # not necessary
```
{% endcode %}
