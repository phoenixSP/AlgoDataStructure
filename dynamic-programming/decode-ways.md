# 🟡 Decode Ways

You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'`\
`"2" -> 'B'`\
`...`\
`"25" -> 'Y'`\
`"26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

* `"AAJF"` with the grouping `(1, 1, 10, 6)`
* `"KJF"` with the grouping `(11, 10, 6)`
* The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.\
\
Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

The first solution looks at recursive implementation.

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        number of ways to decode "12" -> [count(1)*count(2) + count(12)] -> 1*1 + 1 = 2
        number of ways to decode "226" -> [count(2)*decode(26) + count(22)*decode(6)] 
                                       -> [count(2)*[count(2)*count(6) + count(26)] + [count(22)*count(6)]
                                       = [1*[1 + 1] + 1*1] = 3
        number of ways to decode "06" -> [count(0)*count(6) + count(06)] -> 0 + 0 = 0

        Recursive solution: 
        - Assign the base case of the last index. the number of ways that can be decoded is always 1
        - Create a recursive function to check the value at i. The value at i can be value at i+1. If s[i] =='1' or s[i]=='2' and s[i+1]=='6', then value at i += value at i+2

        TC: O(n) as it iterates over each index once
        SC: O(n) 
        '''
        dp = {len(s): 1} # base case: the last index has 1 option

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0

            # run the count for i + s[i+1:]
            res = dfs(i+1)
        
            if i+1 < len(s) and ((s[i]=="1") or \
            (s[i]=='2' and s[i+1] in ["0", "1", "2", "3", "4", "5", "6"])): 
                # theres at least another element after i and theres a number between 10-26
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)
```

The second solution looks at the dynamic programming approach

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        number of ways to decode "12" -> [count(1)*count(2) + count(12)] -> 1*1 + 1 = 2
        number of ways to decode "226" -> [count(2)*decode(26) + count(22)*decode(6)] 
                                       -> [count(2)*[count(2)*count(6) + count(26)] + [count(22)*count(6)]
                                       = [1*[1 + 1] + 1*1] = 3
        number of ways to decode "06" -> [count(0)*count(6) + count(06)] -> 0 + 0 = 0

        Recursive solution: 
        - Assign the base case of the last index. the number of ways that can be decoded is always 1
        - Create a recursive function to check the value at i. The value at i can be value at i+1. If s[i] =='1' or s[i]=='2' and s[i+1]=='6', then value at i += value at i+2

        TC: O(n) as it iterates over each index once
        SC: O(n) 

        Dynamic Programming solution: 
        - We create a dp array of length n+1 because we also want to consider the option of an empty string
        dp[0] = 1 because theres only one way to decode an empty string -> as empty
        dp[1] = 0 if s[1] == '0' else 1

        iterate over the array to calculate the entire length 
        TC: O(n)
        SC: O(n)
        '''
        if not s or s[0] == '0':  # If the string is empty or starts with '0', no valid decoding
            return 0

        n = len(s)
        dp = [0]*(n+1)
        # Base cases
        dp[0] = 1  # Empty string has one way to be decoded
        dp[1] = 1  # First character is guaranteed to have one way to be decoded, since we checked s[0] != '0'
        for i in range(2, n+1):
            print(i)
            if s[i-1] != '0':
                # non zero element
                dp[i] = dp[i-1]

            # get two digits
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n]
```

Space optimized solution

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        number of ways to decode "12" -> [count(1)*count(2) + count(12)] -> 1*1 + 1 = 2
        number of ways to decode "226" -> [count(2)*decode(26) + count(22)*decode(6)] 
                                       -> [count(2)*[count(2)*count(6) + count(26)] + [count(22)*count(6)]
                                       = [1*[1 + 1] + 1*1] = 3
        number of ways to decode "06" -> [count(0)*count(6) + count(06)] -> 0 + 0 = 0

        Recursive solution: 
        - Assign the base case of the last index. the number of ways that can be decoded is always 1
        - Create a recursive function to check the value at i. The value at i can be value at i+1. If s[i] =='1' or s[i]=='2' and s[i+1]=='6', then value at i += value at i+2

        TC: O(n) as it iterates over each index once
        SC: O(n) 

        Dynamic Programming solution: 
        - We create a dp array of length n+1 because we also want to consider the option of an empty string
        dp[0] = 1 because theres only one way to decode an empty string -> as empty
        dp[1] = 0 if s[1] == '0' else 1

        iterate over the array to calculate the entire length 
        TC: O(n)
        SC: O(n)

        Space optimized sol:
        - Since we look at only two values at a time, we can use two vars only to keep track of the last two vals
        TC: O(n)
        SC: O(1)
        '''
        if not s or s[0] == '0':  # If the string is empty or starts with '0', no valid decoding
            return 0

        n = len(s)
        # Base cases
        count1 = 1  # Empty string has one way to be decoded
        count2 = 1  # First character is guaranteed to have one way to be decoded, since we checked s[0] != '0'
        for i in range(2, n+1):
            res = 0
            if s[i-1] != '0':
                # non zero element
                res = count2

            # get two digits
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                res += count1
            count1 = count2
            count2 = res

        return count2
```
