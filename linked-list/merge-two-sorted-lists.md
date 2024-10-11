# 🟢 Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

{% code overflow="wrap" %}
```python
# leetcode 21: https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Solution: 
        - Use a dummy node for the beginning and a pointer tail to point at the last "makeshift" list
        - Point tail to the smaller element of list1 and list2, and move the linked list head to the head 
        - Check at the end if there's any extra elements left in either of the linked lists, and add it to tail

        TC: O(m + n) where m, n are lengths of the linked lists
        SC: O(1)
        '''

        if list1 is None: 
            return list2

        if list2 is None:
            return list1

        dummy = ListNode()
        tail = dummy # pointer to dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                # list1 has the smaller value
                tail.next = list1
                list1 = list1.next # moving the head of list1
            else:
                # list2 has equal value or smaller
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is not None: # check if list1 is longer than list2
            tail.next = list1
        elif list2 is not None: # check if list2 is longer than list1
            tail.next = list2

        return dummy.next
```
{% endcode %}
