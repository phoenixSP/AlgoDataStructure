# 🔴 Merge K sorted lists

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

There are two ways to solve this: One by iteratively merging two linked lists or by using a heap

Solution 1: Iteratively merging two linked lists

```python
# Leetcode 23. https://leetcode.com/problems/merge-k-sorted-lists/

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

Solution 2: Merge linked lists using heap

```python
from heapq import heapify, heappush, heappop
class Solution:
    '''
    Solution: 
    - Use a heap to sort the linked list
    - Add all the first elements
    - While heap still has elements, pop the smallest one, and add it to the dummy list

    TC: O(k) + O(nlogk) because there are always k elements in the heap and the heap loop goes on n times (number of elements)
    SC: O(k)
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        heap = []
        
        for i, lst in enumerate(lists):
            if lst:
                heap.append((lst.val, i, lst))
                lst = lst.next
        
        heapify(heap)

        dummy = ListNode()
        tail = dummy

        while heap:
            value, i, node = heappop(heap)
            tail.next = node 
            node = node.next
            if node:
                heappush(heap, (node.val, i, node))
            tail = tail.next
        
        return dummy.next
```
