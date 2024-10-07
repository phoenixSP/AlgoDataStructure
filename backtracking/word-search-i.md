# 🟡 Word Search I

Given an `m x n` grid of characters `board` and a string `word`, return `true` _if_ `word` _exists in the grid_.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

{% code overflow="wrap" %}
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Solution: 
        - We use backtracking as we need to do dfs on the "graph"/grid
        - Normal DFS is used to traverse only one path without backtracking, whereas backtracking DFS does it differently (by backtracking out of failing paths)
        
        TC: O(m*n*dfs) -> O(m*n*4^L)
        TC of Backtracking dfs = 4^len(word) because each position in the word can lead to 4 potential moves, and that can happen max L times 
        '''
        
        def dfs(i,j, index, visited):

            if index == len(word):
                return True

            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return False

            if board[i][j] == word[index] and (i,j) not in visited:
                visited.add((i,j))
                found = dfs(i+1, j, index+1, visited) or dfs(i, j+1, index+1, visited) or dfs(i-1, j, index+1, visited) or dfs(i, j-1, index+1, visited)
                visited.remove((i,j))

                return found
            
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    visited = set() # item removal TC: O(1)
                    if dfs(i, j, 0, visited):
                        return True
        return False
```
{% endcode %}

## Follow up

Follow up question: Could you use search pruning to make your solution faster with a larger `board`?

Reference (read later): [https://leetcode.com/problems/word-search/solutions/1653308/some-thoughts-about-the-follow-up-pruning/](https://leetcode.com/problems/word-search/solutions/1653308/some-thoughts-about-the-follow-up-pruning/)

1. **Prune 1:**\
   _Return false if the length of the word is greater than the number of cells (R\*C) of the matrix._
2. **Prune 2:**\
   _Return false if the count of any letter in the word exceeds the count of that letter in the matrix. For example: if ‘a’ appears 3 times in the word but only twice in the matrix, the word cannot exist in the puzzle._
3. **Prune 3:**\
   _Count the number of times the first and the last letter of the word appear in the puzzle. if **count(last\_letter) > count (first\_letter)**, reverse the word and then search for it in the puzzle. It helps in minimizing the number of combinations to be checked._

* _For example: **‘abbafcaf’**_\
  _Let’s consider that the first letter ‘a’ appears 4 times in the puzzle while the last letter ‘f’ appears only twice. If we start with ‘a’ as our first letter, in the worst case, we will have to run through all the 4 combinations to match the word._
* _Reversed string: **‘facfababa’**_\
  _With the word reversed, even in the worst case, we will only have to run through 2 combinations to find if the solution exists or not._
