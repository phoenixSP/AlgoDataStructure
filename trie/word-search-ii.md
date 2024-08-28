# 🔴 Word Search II

Given an `m x n` `board` of characters and a list of strings `words`, return _all words on the board_.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Solution

It utilizes the logic of Word Search I for the backtracking DFS and implements trie on top of it.

```python
class TrieNode: 
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for char in word: 
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    '''
        Solution 1:
        - Reuse word search I and iterate over list of words
        - Not optimal

        Solution 2:
        - We can optimize the iteration over the words step using a trie
        
    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, node, word):

            if r < 0 or c < 0 \
            or r >= rows or c >= cols \
            or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visited.remove((r,c))

        rows, cols = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)

        visited = set() # removal TC better
        res = set() # helps with removing duplicates

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)
```

Improvement

* Add pruning&#x20;

