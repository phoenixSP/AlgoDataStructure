# 🟡 Meeting room II

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` where`(s_i < e_i)`, find the minimum number of conference rooms required.\
Note: The end time is exclusive (i.e. not included in the meeting time)\
\
The intuition behind this is as follows:&#x20;

* Sort the list by their start times
* We need to be able to check how many meetings are running when a new meeting starts. To do that, we create a min heap to store the end times. We add the end time of the interval to the heap as it starts.&#x20;
* To implement, we iterate over the sorted list of intervals. Remove the end times that are smaller or equal to the start time of the current interval start time by looping over the heap head.&#x20;
* Add the current interval end time to the heap
* Check the heap size and update the max rooms variable if the current heap length is bigger.

{% code overflow="wrap" %}
```python
import heapq

def find_sets(intervals):

    if intervals is None or len(intervals)==0:
        return 0

    # sort the intervals by their start time
    # O(nlogn)
    intervals = sorted(intervals, key=lambda x: x[0])
    
    max_rooms = 1

    end_times = [intervals[0][1]]
    heapq.heapify(end_times)

    for interval in intervals[1:]:
        while end_times and interval[0] >= end_times[0]:
            # if start time happens earlier than heap end time, the meeting is already over
            heapq.heappop(end_times)
        heapq.heappush(end_times, interval[1])
        max_rooms = max(max_rooms, len(end_times))
    
    return max_rooms
```
{% endcode %}

## Option 2

We can simplify the algorithm if we think of the purpose of the heap: to sort the end times. We sort both our start and end times and iterate over then using two pointers. \
\
Since start time is always greater than the end time, then it ensures that the index of a start time is smaller or equal to the index of the corresponding end time. Thus j is pointing to the end time of an earlier or current meeting, and never a future meeting.&#x20;

```python
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        count = 0
        res = 0

        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])

        ptr1, ptr2 = 0, 0 

        while ptr1 < len(intervals):
            if start_times[ptr1] < end_times[ptr2]:
                ptr1 += 1
                count += 1
            else:
                ptr2 += 1
                count -= 1

            res = max(count, res)

        return res
```
