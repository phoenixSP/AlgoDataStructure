# 🟢 Ransom Note

Given two strings `ransomNote` and `magazine`, return `true` _if_ `ransomNote`_can be constructed by using the letters from_ `magazine` _and_ `false`_otherwise_.

Each letter in `magazine` can only be used once in `ransomNote`.

&#x20;

**Example 1:**

<pre><code><strong>Input: ransomNote = "a", magazine = "b"
</strong><strong>Output: false
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: ransomNote = "aa", magazine = "ab"
</strong><strong>Output: false
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: ransomNote = "aa", magazine = "aab"
</strong><strong>Output: true
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= ransomNote.length, magazine.length <= 105`
* `ransomNote` and `magazine` consist of lowercase English letters.

Always check if strings are only uppercase/lowercase/mixed.

{% code overflow="wrap" %}
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True

        if not magazine:
            return False # ransomnote is non nul

        mag_map = {}
        for ch in magazine:
            mag_map[ch] = mag_map.get(ch, 0) + 1
        
        for ch in ransomNote:
            if ch not in mag_map or mag_map[ch] == 0:
                return False
            
            mag_map[ch] -= 1
        
        return True
```
{% endcode %}
