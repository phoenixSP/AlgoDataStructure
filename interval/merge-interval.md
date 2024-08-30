# 🟡 Merge interval

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return _an array of the non-overlapping intervals that cover all the intervals in the input_.

<pre class="language-python"><code class="lang-python"><strong># Leetcode 56: https://leetcode.com/problems/merge-intervals/description/
</strong><strong>
</strong><strong>class Solution:
</strong>    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Solution: 

        - Problem does not say if the intervals are sorted by their starting times, so sort it first 
        - iterate over sorted intervals and keep track of previous interval
        - if prev_interval ends after current interval starts, merge them and reassign to prev
        - Keep iterating over the intervals list. Prev would be merged with all overlapping intervals
        
        TC: O(nlogn) [sorting] + O(n) [iteration]
        SC: O(n)
        '''
        res = []
        
        # sort 
        intervals = sorted(intervals, key=lambda x: x[0])
    
        prev = intervals[0]
        # iterate
        for i, interval in enumerate(intervals[1:]):
            if prev[1] &#x3C; interval[0]:
                # prev ends before current interval starts
                res.append(prev)
                prev = interval
            else: 
                # prev ends after current interval starts = overlap
                prev = [min(prev[0], interval[0]), max(prev[1], interval[1])]
        
        print(prev)
        res.append(prev)
        
        return res
</code></pre>
