# 🟡 Find Minimum in Rotated Sorted Array

{% code overflow="wrap" %}
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        - If we divide the array into two parts, then the half that has the smallest element
        would have half[0] > half[-1]
        - Keep dividing till we find the minimum
        TC: O(logn)
        '''

        if nums is None or len(nums) == 0:
            return None

        n = len(nums)

        mid = int(n/2)
        start, end = 0, n-1

        minimum = float('inf')

        while start <= end:
            if nums[start] <= nums[end]:
                # the array is sorted, break after checking first element of the subarray
                minimum = min(minimum, nums[start])
                break

            mid = int((start + end)/2)
            minimum = min(minimum, nums[mid])

            if nums[mid] >= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
                
        return minimum
```
{% endcode %}
