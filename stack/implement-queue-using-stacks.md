# 🟢 Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

* `void push(int x)` Pushes element x to the back of the queue.
* `int pop()` Removes the element from the front of the queue and returns it.
* `int peek()` Returns the element at the front of the queue.
* `boolean empty()` Returns `true` if the queue is empty, `false`otherwise.

**Notes:**

* You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
* Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

```python
class MyQueue:
    '''
    Solution: 
    - Use two stacks to emulate the queue operations
    - When pushing items in the queue, push to the first stack
    - When popping or peeping, use the second stack. Pop all elements from the first stack and push them to the second stack. Pop/display the last element from the stack (i.e. the first element added to the queue)

    The operations have an amortized TC of O(1)
    SC: O(n) 
    '''

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x: int) -> None:
        # TC: O(1)
        self.stack1.append(x)

    def _stack_to_queue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        
        if len(self.stack1) > 0 and len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop()) # pop operation is O(1)
        return True

    def pop(self) -> int:
        if self._stack_to_queue():
            return self.stack2.pop()
        return None

    def peek(self) -> int:
        # queue peek checks the first inserted element and stack operations only allow peek operations on the last inserted element
        if self._stack_to_queue():
            return self.stack2[-1]
        return None

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
```
