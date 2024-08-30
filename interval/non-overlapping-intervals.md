# 🟡 Non-overlapping Intervals

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return _the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping_.

Note: if two intervals have the same starting and ending points, they are not considered overlapping

{% code overflow="wrap" %}
```python
# Leetcode 435: https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Solution: 

        Note: if two intervals have the same starting and ending points, they are not considered overlapping

        - Sort the list of intervals 
        - Iterate over the list and keep track of the end of the previous interval
        - If prevEnd <= current_start, there is no overlap. 
            - Else, consider the interval that ends first
            - Update the prevEnd based on the min(prevEnd, currEnd)
            - increase count of interval removal by 1

        TC: O(nlogn) # sorting
        SC: O(n)
        '''

        intervals = sorted(intervals)
        prev_end = intervals[0][1]
        count = 0
        
        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_end = end
            else:
                prev_end = min(end, prev_end)
                count += 1

        return count
```
{% endcode %}
