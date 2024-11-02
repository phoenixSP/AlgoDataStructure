# 🟡 Group Anagrams

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

{% code overflow="wrap" %}
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Brute Force:
        - Sort each string and then check compare if combinations are equal 
        - TC: m^2* nlogn (n=average length of string, m=#of strings)
        
        Another suboptimal solution:
        Get the hashmap of each string and compare the hashmaps of all combinations 

        Optimal solution:
        - Count the characters present in each string and create an array using it. Since we only use lower case alphabets, length of array = 26
        - Use this array as the key and value would be the strings that have that count array

        TC: O(m * n * 26)
        where m = number of strings
        n = average length of strings, to count the characters
        26 because length of array? key retrieval tc? 

        '''
        hashmap = {}
        
        if strs is None or len(strs) == 0:
            return strs

        for string in strs:
            count = [0]*26
        
            for ch in string:
                count[ord(ch)-ord("a")] += 1
            
            if str(count) not in hashmap:
                hashmap[str(count)] = []
        
            hashmap[str(count)].append(string)

        return hashmap.values()
```
{% endcode %}
