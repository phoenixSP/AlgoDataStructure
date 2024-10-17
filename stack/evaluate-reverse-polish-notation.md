# 🟡 Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse\_Polish\_notation).

Evaluate the expression. Return _an integer that represents the value of the expression_.

**Note** that:

* The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
* Each operand may be an integer or another expression.
* The division between two integers always **truncates toward zero**.
* There will not be any division by zero.
* The input represents a valid arithmetic expression in a reverse polish notation.
* The answer and all the intermediate calculations can be represented in a **32-bit** integer.

**Example:**

<pre><code><strong>Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
</strong><strong>Output: 22
</strong><strong>Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
</strong>= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
</code></pre>

```python
class Solution:
    '''
    Solution
    - Use a stack to keep track of the tokens
    - Push token to the stack if its not a operator, if its an operator, pop last two tokens and perform given operation

    TC: O(n)
    SC: O(n)
    '''
    def evalRPN(self, tokens: List[str]) -> int:

        if tokens is None or len(tokens) == 0:
            return None
        
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                res = None
                if token == '+':
                    res = b + a
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = a / b
                stack.append(res)

        return int(stack[0])
```
