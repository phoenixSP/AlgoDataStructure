# 🟡 Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Notice** that you may not slant the container.

&#x20;

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question\_11.jpg)

<pre><code><strong>Input: height = [1,8,6,2,5,4,8,3,7]
</strong><strong>Output: 49
</strong><strong>Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: height = [1,1]
</strong><strong>Output: 1
</strong></code></pre>

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Brute force solution:
        - take all possible combination of heights to calculate the volume
        - for i in range(0, n-1):
            for j in range(i+1, n):
                area = min(heights[i], heights[i])*(j -1)
                get max area

        TC: O(n^2) 
        SC: O(1)

        Optimal solution
        - Take two pointers left and right. The reason is that to make area maximum, we need to maximize 
        width and height, in this case (and the easier option) is to start with start and end of array
        - Calculate area 
        - Move the index that has the minimum height among the two
        TC: O(n)
        SC: O(1)
        '''
        max_area = 0
        if heights is None or len(heights) < 2:
            return max_area

        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:
            area = min(heights[left], heights[right])* (right-left)
            max_area = max(area, max_area)

            if heights[left] < heights[right]:
                left += 1
                
            elif heights[left] > heights[right]:
                right -= 1
            else:
                # condtion if it's equal
                # since we are concerned with the maximum volume, if we move only one pointer, the max it can be is the current volume
                # thus we can move both
                left += 1
                right -= 1
                
        return max_area
        
```
