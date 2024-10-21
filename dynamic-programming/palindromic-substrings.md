# 🟡 Palindromic Substrings

Given a string `s`, return _the number of **palindromic substrings** in it_. A string is a **palindrome** when it reads the same backward as forward. A **substring** is a contiguous sequence of characters within the string.

The following solution uses DP, but the expansion from center algo from longest palindromic substring can also be used to calculate the palindromic substrings.&#x20;

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        - Task: count the num of palindromic substrings
        Brute force:
        - extract all substrings and check if they are palindromes or not
        - O(n^2)*O(n) -> O(n^3)

        For palindromic substring, we can say if s[i+1: j-1] is a palindrome, and s[i] == s[j], then s[i:j] is also a palindrome
        
        Solution: 
        - DP solution
        - initialize dp 2D array, and count vars
        - Check the length 1 strings (they are palindromes)
        - Check length 2 palindromes
        - iterate over s and fill out the dp array

        TC: O(n^2)
        SC: O(n^2)
        '''

        if s is None or len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                count += 1
                dp[i][i+1] = True
        
        # k = length of substring
        for k in range(3, n+1):
            for left in range(n-k+1):
                right =  k + left - 1 # length = right - left + 1
                if dp[left+1][right-1] and s[left] == s[right]:
                    dp[left][right] = True
                    count += 1

        return count
```
