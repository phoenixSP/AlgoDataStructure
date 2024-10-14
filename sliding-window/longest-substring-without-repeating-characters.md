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
        Rough: 

        LENGTH of LONGEST SUBSTRING without repeating characters
        Dictionary to keep characters in window and their index
        Once a character is repeated, we can move window to min(index+1, right)
        Make sure to remove all the characters that were moved out of the window

        left = min(index+1, right)
        right += 1

        abcabcbb -> window: abc; length 3; map-> (a,3), (b,4), (c,2), 


        Solution:
        - Define sliding window starting and ending at 0, and a char map for the curr window
        - keep incrementing right till last occurence of char
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
        
        if len(s) == 1:
            return 1

        window = {}
        left, right=0, 0
        length = 0

        while right < len(s):

            char = s[right]
            if char in window:
                # move left to last char occurence and remove chars
                last_occurence = window[char]
                while left <= last_occurence:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]] #O(1)
                    left += 1
            window[char] = right
            length = max(length, right - left + 1)
            right += 1
        
        return length
```
{% endcode %}
