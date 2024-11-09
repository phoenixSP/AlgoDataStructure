# 🟢 Flood Fill

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**:

1. Begin with the starting pixel and change its color to `color`.
2. Perform the same process for each pixel that is **directly adjacent**(pixels that share a side with the original pixel, either horizontally or vertically) and shares the **same color** as the starting pixel.
3. Keep **repeating** this process by checking neighboring pixels of the _updated_ pixels and modifying their color if it matches the original color of the starting pixel.
4. The process **stops** when there are **no more** adjacent pixels of the original color to update.

Return the **modified** image after performing the flood fill.

&#x20;

**Example 1:**

**Input:** image = \[\[1,1,1],\[1,1,0],\[1,0,1]], sr = 1, sc = 1, color = 2

**Output:** \[\[2,2,2],\[2,2,0],\[2,0,1]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

From the center of the image with position `(sr, sc) = (1, 1)` (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is **not** colored 2, because it is not horizontally or vertically connected to the starting pixel.

**Example 2:**

**Input:** image = \[\[0,0,0],\[0,0,0]], sr = 0, sc = 0, color = 0

**Output:** \[\[0,0,0],\[0,0,0]]

**Explanation:**

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

**Constraints:**

* `m == image.length`
* `n == image[i].length`
* `1 <= m, n <= 50`
* `0 <= image[i][j], color < 216`
* `0 <= sr < m`
* `0 <= sc < n`

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
