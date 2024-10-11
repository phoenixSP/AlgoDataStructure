# 🟢 Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

{% code overflow="wrap" %}
```python
# leetcode 206: https://leetcode.com/problems/reverse-linked-list/description/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Solution: 
        - For reversing a linked list without any extra storage (of O(n) scale), we have to use two pointers prev and next
        - prev points to the earlier node and next points to the next node
        - get next's pointer before changing curr.next to prev, and assign curr to prev and next to curr. 
        
        TC: O(n) iterates over the entire linked list
        SC: O(1)
        '''
        # empty linked list
        if head is None: 
            return head

        prev = None 
        curr = head
        while curr is not None:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head
```
{% endcode %}
