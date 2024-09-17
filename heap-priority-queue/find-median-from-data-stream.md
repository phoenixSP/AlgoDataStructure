# 🔴 Find Median from Data Stream

Implement the MedianFinder class:

* `MedianFinder()` initializes the `MedianFinder` object.
* `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
* `double findMedian()` returns the median of all elements so far. Answers within `10-5` of the actual answer will be accepted.

{% code overflow="wrap" %}
```python
# Leetcode 295: https://leetcode.com/problems/find-median-from-data-stream/description/

from heapq import heappush, heappop
class MedianFinder:
    '''
    Brute force solution is to maintain a sorted array while adding the elements. This makes the sorting O(n) where n is current length and median calculation O(1). We can improve the sorting (sort of) better by using heaps. 

    Solution: 
    - Maintain two heaps, a max heap and a min heap. The maxHeap contains all the numbers to the left/including median and the minHeap contains the numbers to greater/including the median
    - Insert each number into the max heap if it is smaller than the root of the max heap, and into the min heap otherwise
    - Balance the heaps by transfering the roots between the heaps
    - Calculate the median by taking the average of the roots of both heaps if they are of equal size, or by taking the root of the max heap otherwise.

    TC: Number addition O(logn); Median calculation O(1)
    SC: O(n)
    '''

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
    def addNum(self, num: int) -> None:

        if self.max_heap and num < -self.max_heap[0]:
            heappush(self.max_heap, -num) # python heaps are minheaps
        else:
            heappush(self.min_heap, num)

        # rebalance: the difference between the sizes would always be 1, with maxHeap having the extra element
    
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return 0.5*(-self.max_heap[0] + self.min_heap[0])
```
{% endcode %}



## Follow up 1 and 2

1. If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
2. If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

```python
class MedianFinder:
    '''
    Follow up 1: 

    - Use a counter for count of the incoming numbers and keep track of total count
    - Median is position total_count//2 + 1 if total_count is odd, else average of total_count/2 and total_count/2 + 1 positions

    TC: O(1) 
    SC: O(1) # constant length array

    Follow up 2:
    - Since 99% of the numbers fall in the same range, we can use the same algo and keep track of the number of data points that are smaller the 0 or greater than 100. The median will shift #bigger - #smaller to the right
    '''

    def __init__(self):
        self.counter = [0]* 6
        self.total_counter = 0
        

    def addNum(self, num: int) -> None:
        self.counter[num] += 1
        self.total_counter += 1

    def findMedian(self) -> float:
        temp_counter = 0
        print(self.counter, self.total_counter)

        if self.total_counter % 2 == 1:
            for i, count in enumerate(self.counter):
                temp_counter += count
                if temp_counter >= (self.total_counter//2 + 1):
                    return i
        else:
            mid_index_1 = self.total_counter/2 
            mid_index_2 = self.total_counter/2 + 1

            median_1 = median_2 = None

            for i, count in enumerate(self.counter):
                temp_counter += count
                if temp_counter >= mid_index_1 and median_1 is None:
                    median_1 = i
                if temp_counter >= mid_index_2:
                    median_2 = i
                    
                    print(median_1, median_2)
                    return 0.5*(median_1 + median_2)

```
