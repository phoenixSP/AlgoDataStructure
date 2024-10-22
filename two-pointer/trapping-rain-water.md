# 🔴 Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

<pre><code><strong>Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
</strong><strong>Output: 6
</strong><strong>Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: height = [4,2,0,3,2,5]
</strong><strong>Output: 9
</strong></code></pre>

**Constraints:**

* `n == height.length`
* `1 <= n <= 2 * 104`
* `0 <= height[i] <= 105`

{% code overflow="wrap" %}
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Thought process: Think of the heights as edges of the container. leftMax is the max of the left hand side seen till now and rightMax is the max of the right handside seen till right. Now, left has two (or three) potential boundaries: right, max between right and left that is the true right max and leftMax. Now, the water at left is determined by the smallest boundary. If right > left, then it means left is already smaller than right Now the leftMax becomes the left edge of the container, and its height of water is now determined by the leftMax.
        Water is determinded by the leftMax when left < right because even if rightMax has the potential to be larger than right, the max water height will be limited by left.. so to check how much water left can have, we have to look at the left side max.

        TC: O(n)
        SC: O(1)
        '''

        if height is None or len(height) == 0:
            return 0
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]

        water = 0
        while left < right:
            if height[left] < height[right]:
                water += max(leftMax - height[left], 0)
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                water += max(rightMax - height[right], 0)
                rightMax = max(rightMax, height[right])
                right -= 1
        
        return water
```
{% endcode %}
