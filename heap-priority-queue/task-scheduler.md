# 🟡 Task Scheduler

You are given an array of CPU `tasks`, each represented by letters A to Z, and a cooling time, `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: **identical** tasks must be separated by at least `n` intervals due to cooling time.

​Return the _minimum number of intervals_ required to complete all tasks.

{% code overflow="wrap" %}
```python
from heapq import heappush, heappop, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Solution: 
        - Create a frequency counter for the tasks
        - The tasks that occur most frequently should be picked up first, so that the other tasks can be fit in their cooling times for optimal results (least total time)
        - We use a maxHeap to pick the task with the highest frequency each time in O(log m) m being the number of unique tasks
        - Create a max Heap of all the frequencies
        - Pop the task with most frequency, decrease its count and add it to the queue along with the time when it can be picked up again (current time+n)
        - Check the queue, if the topmost element is ready to be picked up, add it back to the maxheap again
        n = Number of tasks
        m = Number of unique tasks 
        idle = idle time
        TC Explanation: 
        Total TC: O(n) [counter set up] + second loop

        Second loop TC: O(n*idle_time*logm)
        If m and idle are similar/small, idle times are utilized to perform other tasks, thus TC of second loop = O(n*logm). Now m is 26, so this reduces to O(n). 
        In worst case scenario, m=small and idle time comparitively large, TC becomes O(n*idle_time)

        Finally, TC: O(n)
        SC: O(n)
        '''

        if tasks is None or len(tasks) == 0:
            return 0 

        counter = {}
        for task in tasks:
            if task not in counter: 
                counter[task] = 0
            counter[task] += 1
        
        maxHeap = [-count for count in counter.values()]
        heapify(maxHeap)

        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1
            if maxHeap:
                # current task = task being popped
                count = 1 + heappop(maxHeap) # Adding 1 because frequency is negative
                if count: # only add to queue if count > 0
                    queue.append([count, time+n])

            # the queue is used to add back the task after its cooling time
            if queue and queue[0][1] == time:
                heappush(maxHeap, queue.popleft()[0])

        return time
```
{% endcode %}
