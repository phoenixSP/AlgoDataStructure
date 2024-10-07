# 🟢 Last Stone Weight

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

* If `x == y`, both stones are destroyed, and
* If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return _the weight of the last remaining stone_. If there are no stones left, return `0`.

{% code overflow="wrap" %}
```python
from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Solution: 
        - Create a heap with all the stones array (default is minHeap, so add the elements with a negative)
        - At each iteration pop top 2 elements and perform subtraction operation, add the remainder stone weight
        - Iterate till the length of heap > 1
        - Check if heap has one element, then return it, else return 0 

        TC: O(n) #heapify + O(n*logn) = O(nlogn)
        SC: O(n) #heap
        '''

        if stones is None or len(stones) == 0:
            return 0 

        if len(stones) == 1:
            return stones[0]

        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            stone1 = heappop(heap)
            stone2 = heappop(heap)

            new_stone = stone1 - stone2
            if new_stone != 0:
                heappush(heap, new_stone)
            
        if len(heap) > 0:
            return -heap[0]
        else:
            return 0
```
{% endcode %}
