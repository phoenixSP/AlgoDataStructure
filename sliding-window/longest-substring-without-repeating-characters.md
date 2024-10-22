# 🟡 Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest** **substring** without repeating characters.

**Example 1:**

<pre><code><strong>Input: s = "abcabcbb"
</strong><strong>Output: 3
</strong><strong>Explanation: The answer is "abc", with the length of 3.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "bbbbb"
</strong><strong>Output: 1
</strong><strong>Explanation: The answer is "b", with the length of 1.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: s = "pwwkew"
</strong><strong>Output: 3
</strong><strong>Explanation: The answer is "wke", with the length of 3.
</strong>Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
</code></pre>

**Constraints:**

* `0 <= s.length <= 5 * 104`
* `s` consists of English letters, digits, symbols and spaces.

{% code overflow="wrap" %}
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Solution:
        - Define sliding window starting and ending at 0, and a char set for the curr window
        - keep incrementing right while curr char is not in set
        - If char in set, remove all characters present in window till (and including) curr char
        - Update left and right accordingly

        TC: O(n)
        SC: O(1)

        Note:
        Make sure to remove all characters in the current window till repeat

        For eg, if a b c a is the string, when right comes to a, our window becomes 
        "a". Since previous window was "abc", we have to make sure we don't have b and c
        in the dictionary/set.
        '''

        if s is None or len(s) == 0:
            return 0 

        char_set = set()
        left, right = 0, 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            while char in char_set: # 
                char_set.remove(s[left])
                left += 1
            
            char_set.add(char)
            max_len = max(max_len, right - left + 1)
            
        return max_len        
```
{% endcode %}
