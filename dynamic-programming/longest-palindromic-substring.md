# 🟡 Longest Palindromic Substring

Given a string `s`, return _the longest_ _palindromic_ _substring_ in `s`.

**Example 1:**

<pre><code><strong>Input: s = "babad"
</strong><strong>Output: "bab"
</strong><strong>Explanation: "aba" is also a valid answer.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "cbbd"
</strong><strong>Output: "bb"
</strong></code></pre>

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consist of only digits and English letters.

There are two solutions discussed here: One is a DP solution, other is an expansion from center solution. Both take O(n^2) time to complete.&#x20;

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Brute Force solution: 
        - Choose all characters and start a substring till the end for each
        - Check if the substring is a palindrome
        - Choosing all characters = O(n^2) and checking if substring is palindrome = O(n) -> TC: O(n^3)
        
        Dynamic Programming solution: 
        - A substring s[i:j] is a palindrome, if s[i+1:j-1] is a palindrome and s[i] == s[j]
        - So, we have to keep a track of the value of s[i+1:j-1] using a 2D table
        - Check the length 1 and length 2 subcases first
        - Then check substrings of length >= 3

        TC: O(n^2)
        SC: O(n^2)
        '''

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        maxlen = 0
        start = 0

        for i in range(n): # strings of length 1 are always palindrome
            dp[i][i] = True
            start = i
            maxlen = 1
        
        for i in range(n-1): # base case of even length palindromes
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                maxlen = 2

        # k = length variable
        for k in range(3, n+1): 
            for left in range(n - k + 1):
                right = left + k - 1   # length = r - l + 1
                if dp[left+1][right-1] and s[left] == s[right]:
                    dp[left][right] = True
                    if k > maxlen:
                        maxlen = k
                        start = left
        
        return s[start: start + maxlen]
```

The solution using expansion for center is below

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Brute Force solution: 
        - Choose all characters and start a substring till the end for each
        - Check if the substring is a palindrome
        - Choosing all characters = O(n^2) and checking if substring is palindrome = O(n) -> TC: O(n^3)
        
        Expansion from the center solution: 
        - The brute force solution can be optimized if the substring is traversed from the center to its edges, i.e. start from index i and expand to i-1 and i+1 and so on
        - if s[i-1] and s[i+1] are same, then the substring is a palindrome
        - Note that this only considers the odd sized palindromes. We have to use a different case to figure out even sized palindromes

        TC: O(n^2)
        SC: O(1)
        '''
        n = len(s)
        maxlen = 0
        start = 0

        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if maxlen < (right - left + 1):
                    maxlen = right - left + 1
                    start = left 
                left -= 1
                right += 1
            
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                if maxlen < (right - left + 1):
                    maxlen = right - left + 1
                    start = left 
                left -= 1
                right += 1
        
        return s[start: start+maxlen]
```

