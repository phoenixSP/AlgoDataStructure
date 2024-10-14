# 🟡 Longest Repeating Character Replacement

Intuitive solution&#x20;

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

                # recalulcate majority count O(26)
                for ch in window:
                    majority_count = max(majority_count, window[s[left]])

                # calculat
            length = max(length, right - left + 1)
            right += 1

        return length
```

Slightly optimized solution: TC remains the same&#x20;

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

