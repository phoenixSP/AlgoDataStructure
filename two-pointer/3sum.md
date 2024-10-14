# 🟡 3Sum

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

<pre><code><strong>Input: nums = [-1,0,1,2,-1,-4]
</strong><strong>Output: [[-1,-1,2],[-1,0,1]]
</strong><strong>Explanation: 
</strong>nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [0,1,1]
</strong><strong>Output: []
</strong><strong>Explanation: The only possible triplet does not sum up to 0.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: nums = [0,0,0]
</strong><strong>Output: [[0,0,0]]
</strong><strong>Explanation: The only possible triplet sums up to 0.
</strong></code></pre>

{% code overflow="wrap" %}
```python
 class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        if nums is None or len(nums) < 3:
            return output

        nums = sorted(nums)

        if nums[0] > 0: 
            return output

        n = len(nums)

        for i in range(n-2):
            # i is the beginning
            left = i + 1
            right = n - 1

            while left < right:

                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else: 
                    output.add((nums[i], nums[left], nums[right])) # O(1) average
                    left += 1
                    right -= 1
        
        return output
```
{% endcode %}

Slightly optimized solution

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Brute force Solution:
        - run three loops over the array 
        for i in range(0, n-2):
            for j in range(i, n-1):
                for k in range(j, n):
                    <add operation>
        TC: O(n^3)
        SC: O(1)

        Solution: 
        - Sort array
        - Iterate over array using i and use rest of to find the -nums[i] elements
        (two sum problem)
        - Solve it using two pointers, left at i+1 and right at n-1
        - When found a match, update left and make sure to ignore duplicates 
        '''
        output = []
        if nums is None or len(nums) == 0:
            return output
        
        nums = sorted(nums)

        if nums[0] > 0:
            # smallest number is positive, 0 sum is not possible
            return output

        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                # ignoring duplicate 
                continue
            left = i + 1
            right = len(nums) - 1
            
            

            while left < right:
                
                    
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1

                    # can ignore this part; makes it super optimal
                    while nums[left-1] == nums[left] and left < right:
                        # ignoring duplicates
                        left += 1

        return output
```
