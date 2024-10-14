# 🔴 Trapping Rain Water



```python
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
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
