# 🔴 Merge K sorted lists

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

The first solution uses heaps to merge K sorted lists.&#x20;

{% code overflow="wrap" %}
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    '''
    Brute Force solution: 
    Sort the current elements of all the lists each time we look at a new element (TC O(k)). This can be optimized using min heaps.
    
    Solution: 
    Since the individual lists are all sorted, we can take the top elements of each array and use a minHeap to find their minimum. Pop the minimum and add the next element of the array that the minimum came from. Keep doing this until all the arrays have been traversed. The elements are popped in order.

    TC: O(nlogk) where n = total number of elements
    SC: O(k)
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        
        heap = []

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy

        while heap: 
            val, i, node = heappop(heap)
            curr.next = node
            curr = node
            node = node.next

            if node:
                heappush(heap, (node.val, i, node))

        return dummy.next
```
{% endcode %}

The second solution looks at a merge sort style solution.

{% code overflow="wrap" %}
```python
class Solution:
    '''
    Solution: 
    Reduce the problem to a "merge 2 lists" problem by taking two lists at a time and merging them till there is only 1 list left. This is inspired by merge sort.

    TC: O(nlogk) where n = total number of elements
    SC: O(k)
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None # checking edge case
                merged_lists.append(self.merge2Lists(l1, l2))
            lists = merged_lists

        return lists[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next 
            curr = curr.next 
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
```
{% endcode %}
