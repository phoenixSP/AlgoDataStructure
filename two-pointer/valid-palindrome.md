# 🟢 Valid Palindrome

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` _if it is a **palindrome**, or_ `false` _otherwise_.

**Example 1:**

<pre><code><strong>Input: s = "A man, a plan, a canal: Panama"
</strong><strong>Output: true
</strong><strong>Explanation: "amanaplanacanalpanama" is a palindrome.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "race a car"
</strong><strong>Output: false
</strong><strong>Explanation: "raceacar" is not a palindrome.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: s = " "
</strong><strong>Output: true
</strong><strong>Explanation: s is an empty string "" after removing non-alphanumeric characters.
</strong>Since an empty string reads the same forward and backward, it is a palindrome.
</code></pre>

**Constraints:**

* `1 <= s.length <= 2 * 105`
* `s` consists only of printable ASCII characters.

{% code overflow="wrap" %}
```python
class Solution:
    def alphanum(self, ch):
        if ((ord('A') <= ord(ch) <= ord('Z'))
        or (ord('a') <= ord(ch) <= ord('z'))
        or (ord('0') <=ord(ch) <= ord('9'))        
        ):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        # Can use str.isalnum() as well
        if s is None or len(s) == 0: # the constraint states that len(s)>1
            return False

        i = 0
        j = len(s) - 1

        while i < j:
            if not self.alphanum(s[i]):
                i += 1
            elif not self.alphanum(s[j]):
                j -= 1
            elif s[i].lower() !=s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True
```
{% endcode %}
