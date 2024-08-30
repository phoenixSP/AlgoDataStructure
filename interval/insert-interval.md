# 🟡 Insert interval

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith`interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` _after the insertion_.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

```python
# Leetcode 57: https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Solution: 
        - Iterate over the intervals
        - If the current interval starts after the newInterval ends, you can add newInterval and all remaining intervals to the result and return it
        - if the current interval ends before newInterval starts, then add current interval to the result
        - In all other cases, the current interval overlaps with the newInterval, so merge is necessary. We should not add the merged interval right away, as it may be overlapping with multiple following intervals

        Note that the intervals are sorted, otherwise we would need to sort it.

        TC: O(n) 
        SC: O(n)
        '''

        def merge_overlap(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        res = []
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                # curr interval starts after new interval ends
                # there's no overlap with the previous interval, so it is added as is
                res.append(newInterval) 
                return res + intervals[i:]

            elif interval[1] < newInterval[0]:
                # curr interval ends before new interval starts
                res.append(interval)
            else: 
                # If the new interval overlaps with 2 intervals, then this else is called twice
                newInterval = merge_overlap(interval, newInterval)
            
        # if newinterval at end, add it now
        res.append(newInterval)

        return res
```
