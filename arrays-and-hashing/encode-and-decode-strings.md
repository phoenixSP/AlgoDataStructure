# 🟡 Encode and decode strings

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement `encode` and `decode`

**Example 1:**

```java
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
```

**Example 2:**

```java
Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
```

**Constraints:**

* `0 <= strs.length < 100`
* `0 <= strs[i].length < 200`
* `strs[i]` contains only UTF-8 characters.

{% code overflow="wrap" %}
```python
class Solution:
    '''
    - Use the length of string and a delimiter before the string 
    TC: O(n), SC: O(n)
    '''

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] != "#": 
                # for the last letter of the last word, s[j] would not be equal to #, hence j would become out of bounds, hence we need the j bound
                j += 1

            length = int(str(s[i:j]))
            res.append(str(s[j+1: j+1+length])) # j+1 because j has #
            
            i = j+1+length

        return res
```
{% endcode %}
