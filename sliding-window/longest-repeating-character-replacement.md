# 🟡 Longest Repeating Character Replacement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return _the length of the longest substring containing the same letter you can get after performing the above operations_.

&#x20;

**Example 1:**

<pre><code><strong>Input: s = "ABAB", k = 2
</strong><strong>Output: 4
</strong><strong>Explanation: Replace the two 'A's with two 'B's or vice versa.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "AABABBA", k = 1
</strong><strong>Output: 4
</strong><strong>Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
</strong>The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 105`
* `s` consists of only uppercase English letters.
* `0 <= k <= s.length`

Intuitive solution&#x20;

{% code overflow="wrap" %}
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Notepad:

        s -> string, k -> allowed number of replacements
        So if we want the longest substring with k replacements, we have to keep a note of the majority character in the window. Everything else would have to be covered by the k replacements

        so let's consider a window.. with left and right pointers and a window directory with count vals
        when we look at right, check if char is in dict
        - if char in dict, increment count.
        - if char not in dict, add it to the dict
        count the major element.. to do this, check the majority count before. if the new char count > previous, update majority count 
        while length of window - majority_count > k, increment left and update window counts
        - recalculate majority count
        - calculate length when the window is valid again

        TC: O(n)
        SC: O(n) if window spans the complete sequence


        '''

        if s is None or len(s) == 0:
            return 0 

        if len(s) < k:
            return len(s)

        left, right = 0, 0
        window = {}
        length = 0
        majority_count = 0

        while right < len(s):
            char = s[right]
            if char not in window:
                # check majority 
                window[char] = 0
            window[char] += 1
            majority_count = max(majority_count, window[char])

            while (right - left + 1) - majority_count > k:
                # extra chars
                window[s[left]] -= 1
                left += 1

                # this is wrong
                # and unnecessary. If we saw a window with x max freq, we would compare all subsequent windows with that freq, until we find a bigger window. So always update the length if case its bigger
                # # recalulcate majority count O(26) = O(1)
                # for ch in window:
                #     majority_count = max(majority_count, window[s[left]])

            length = max(length, right - left + 1)
            right += 1

        return length
```
{% endcode %}

Slightly optimized solution: TC remains the same (exactly same now: update 11/04)

{% code overflow="wrap" %}
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Notepad:

        s -> string, k -> allowed number of replacements
        So if we want the longest substring with k replacements, we have to keep a note of the majority character in the window. Everything else would have to be covered by the k replacements

        so let's consider a window.. with left and right pointers and a window directory with count vals
        when we look at right, check if char is in dict
        - if char in dict, increment count.
        - if char not in dict, add it to the dict
        count the major element.. to do this, check the majority count before. if the new char count > previous, update majority count 
        while length of window - majority_count > k, increment left and update window counts
        - The validity of the window is not checked everytime.. because we need to update the length only when we find another window with character with bigger majority count.. otherwise only make sure that the window length is consistent. ie. length - max_freq < k
        - calculate length when the window is valid again

        TC: O(n)
        SC: O(n) if window spans the complete sequence


        '''

        if s is None or len(s) == 0:
            return 0 

        if len(s) < k:
            return len(s)

        left, right = 0, 0
        window = {}
        length = 0
        majority_count = 0

        while right < len(s):
            char = s[right]
            if char not in window:
                # check majority 
                window[char] = 0
            window[char] += 1
            majority_count = max(majority_count, window[char])

            while (right - left + 1) - majority_count > k:
                # extra chars
                window[s[left]] -= 1
                left += 1
            length = max(length, right - left + 1)
            right += 1

        return length
```
{% endcode %}

