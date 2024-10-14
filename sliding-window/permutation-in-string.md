# 🟡 Permutation in String

Given two strings `s1` and `s2`, return `true` if `s2` contains a&#x20;

permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:**

<pre><code><strong>Input: s1 = "ab", s2 = "eidbaooo"
</strong><strong>Output: true
</strong><strong>Explanation: s2 contains one permutation of s1 ("ba").
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s1 = "ab", s2 = "eidboaoo"
</strong><strong>Output: false
</strong></code></pre>

**Constraints:**

* `1 <= s1.length, s2.length <= 104`
* `s1` and `s2` consist of lowercase English letters.

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        - Check if any substring within s2 has the same character map as s1
        - Brute force O(n^2) generates all substring within s2 and checks each
        - Sliding window approach
        TC: O(n)
        SC: Since there are 26 characters, thus length of dictionaries can be max 26, hence, O(1)

        '''
        if len(s1) > len(s2):
            return False 
            
        charmap_s1 = {}
        for ch in s1:
            charmap_s1[ch] = charmap_s1.get(ch, 0) + 1
        
        left, right = 0, len(s2)- 1
        check = 0 
        charmap_window = {}
        
        for right in range(len(s2)):
            ch = s2[right]
            charmap_window[ch] = charmap_window.get(ch, 0) + 1

            if ch in charmap_s1 and charmap_window[ch] == charmap_s1[ch]:
                check += 1

            while check == len(charmap_s1):
                # all characters accounted for
                if len(s1) == (right - left + 1):
                    return True

                ch_left = s2[left]
                charmap_window[ch_left] -= 1
                left += 1

                if ch_left in charmap_s1 and charmap_window[ch_left] < charmap_s1[ch_left]:
                    check -= 1
                
        return False
```
