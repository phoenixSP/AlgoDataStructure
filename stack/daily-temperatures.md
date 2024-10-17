# 🟡 Daily Temperatures

Given an array of integers `temperatures` represents the daily temperatures, return _an array_ `answer` _such that_ `answer[i]` _is the number of days you have to wait after the_ `ith` _day to get a warmer temperature_. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**

<pre><code><strong>Input: temperatures = [73,74,75,71,69,72,76,73]
</strong><strong>Output: [1,1,4,2,1,1,0,0]
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: temperatures = [30,40,50,60]
</strong><strong>Output: [1,1,1,0]
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: temperatures = [30,60,90]
</strong><strong>Output: [1,1,0]
</strong></code></pre>

{% code overflow="wrap" %}
```python
class Solution:
'''
Solution: 

- Use the stack to keep track of the past values
- whenever the current value becomes more that stack top, then we pop the stack top and count the indedx difference between current and stack top
- Repeat this till the condition is no longer true
- The last higest temp and last temp would be 0 
'''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        answer = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                answer[stack_index] = i - stack_index
            stack.append((temp, i))
        return answer
```
{% endcode %}
