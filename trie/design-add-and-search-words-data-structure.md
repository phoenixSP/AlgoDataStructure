# 🟡 Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

* `WordDictionary()` Initializes the object.
* `void addWord(word)` Adds `word` to the data structure, it can be matched later.
* `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

```python
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if not curr.children[ord(ch)-ord('a')]:
                curr.children[ord(ch)-ord('a')] = TrieNode()
            curr = curr.children[ord(ch)-ord('a')]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
    
        def search_util(node, word, index):
            '''
            node is the starting point of the search
            '''
            if not node:
                return False
            
            if index == len(word):
                return node.endOfWord
            
            ch = word[index]
            found = False
            if ch == '.':
                for child in node.children:
                    if child:
                        found = search_util(child, word, index+1)
                        if found:
                            return True
                if not found:
                    return False

            if not node.children[ord(ch)-ord('a')]:
                return False
            
            return search_util(node.children[ord(ch)-ord('a')], word, index+1)
        return search_util(self.root, word, 0)
```
