# 🟢 Longest Palindrome

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1

        char_map = {}
        length = 0
        odd = 0

        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1
            if char_map[ch] % 2 == 0:
                length += 2
        
        for ch in char_map:
            if char_map[ch] % 2 == 1:
                odd = 1
                break

        return odd + length 
```
