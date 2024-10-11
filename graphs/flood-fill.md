# 🟢 Flood Fill

{% code overflow="wrap" %}
```python
# Leetcode 733: https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        - The starting point is given, the task is to change the color of the graph component to the new color
        - Perform DFS from the starting component and keep changing the color

        TC: O(|V| + |E|) these numbers reflect the connected component
        SC: O(1) no extra memory
        '''
        # base condition
        if image is None or len(image) == 0:
            return image
        
        n_rows, n_cols = len(image), len(image[0])
        prev_color = image[sr][sc]
        visited = set()

        def dfs(i, j, visited):
            # check conditions

            if (i < 0 or j < 0 or \
            i >= n_rows or j >= n_cols or \
            (i,j) in visited or \
            image[i][j] != prev_color):
                return

            visited.add((i, j))
            image[i][j] = color
            dfs(i+1, j, visited)
            dfs(i, j+1, visited)
            dfs(i-1, j, visited)
            dfs(i, j-1, visited)

            return 

        dfs(sr, sc, visited)

        return image
```
{% endcode %}
