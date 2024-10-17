# 🟡 Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

* `MinStack()` initializes the stack object.
* `void push(int val)` pushes the element `val` onto the stack.
* `void pop()` removes the element on the top of the stack.
* `int top()` gets the top element of the stack.
* `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

```python
class MinStack:
    '''
    Solution: 
    - Implement stack where push, pop, top and getmin operations are all O(1)
    - To make getMin operation to be O(1), we need to have a sorted array (heap would have O(logn) TC)
    - A variable to check min when elements are being inserted would have O(1) TC, but the min would need to be recalculated after popping. That's why we need to save all the previous mins.
    - We would also need to store the order of insertion in the stack
    
    TC: O(1)
    SC: O(n) # general SC
    '''
    def __init__(self):
        self.arr = []
        self.min = math.inf
        self.prevMins = []
        
    def push(self, val: int) -> None:
        self.arr.append(val)
        if val <= self.min: # since we do the equality check as well, we have the same value twice if they were pushed
            self.prevMins.append(self.min) 
            self.min = val

    def pop(self) -> None:
        if len(self.arr) == 0:
            return None
        
        if self.min == self.arr[-1]:
            self.min = self.prevMins.pop()
        self.arr.pop()
            
    def top(self) -> int:
        if len(self.arr) >0:
            return self.arr[-1]
        return None
        
    def getMin(self) -> int:
        return self.min

```
