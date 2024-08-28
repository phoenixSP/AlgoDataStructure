# 🟢 Valid Anagram

Given two strings `s` and `t`, return `true` _if_ `t` _is an anagram of_ `s`_, and_ `false` _otherwise_.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution: def isAnagram(self, s: str, t: str) -> bool: if s is None and t is None: return True

{% code overflow="wrap" %}
```python
class Solution: 
    def isAnagram(self, s: str, t: str) -> bool: if s is None and t is None: return True
        if len(s) != len(t):
            return False
    
        dict_s = {}
        dict_t = {}
    
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1
    
        for ch in dict_s:
            if dict_s[ch] != dict_t.get(ch, 0):
                return False
            # this part is not needed because we only need to check equivalence
            # The next part is needed only when there's a possibility that dict_t has extra characters than dict_s. 
            # That cannot happen as we have seen all characters in dict_s present in dict_t, i.e. number of characters matched till now are same
            # If dict_t has more chars, it is a contradiction of the length equality of the two strings. Hence checking earlier condition is enough
            
            # if ch not in dict_t:
            #     return False
            # elif dict_s[ch] != dict_t[ch]:
            #     return False
            # else:
            #     dict_t.pop(ch)
    
        # if len(dict_t) != 0:
        #     return False
    
        return True
```
{% endcode %}
