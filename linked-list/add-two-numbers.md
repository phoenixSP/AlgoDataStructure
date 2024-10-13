# 🟡 Add two numbers

You are given two **non-empty** linked lists, `l1` and `l2`, where each represents a non-negative integer.

The digits are stored in **reverse order**, e.g. the number 123 is represented as `3 -> 2 -> 1 ->` in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

{% code overflow="wrap" %}
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            add = v1 + v2 + carry
            carry = add//10
            val = add%10

            curr.next = ListNode(val)
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```
{% endcode %}
