# 🟡 Remove Nth Node From End of List

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

```python
# leetcode 19: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Solution:
        - Start traversing the ll. Keep count of the number of nodes being traversed
        - Create a dummy node that points to head. This is useful in cases we have to remove the head
        - Assign ptr1 and ptr2 to the head and dummy
        - Move ptr1 n times
        - Now, move both ptr1 and ptr2 till ptr1 becomes None
        - ptr1 should point to the node before the nth node
        - remove nth node
        - return dummy.next

        Note: this is a single pass solution

        TC: O(n)
        SC: O(1)
        '''
        
        if head is None or head.next is None: # empty ll, or single node in ll
            return None

        dummy = ListNode(0, head)
        ptr1, ptr2 = head, dummy

        for _ in range(n):
            ptr1 = ptr1.next

        while ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # remove nth node from end
        ptr2.next = ptr2.next.next

        return dummy.next
```
