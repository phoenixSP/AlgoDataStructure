# 🟢 Merge Sorted Array

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Solution: 
        - Start from the end of both lists
        - 
        """
        if m == 0:
            nums1[:] = nums2[:] # we cant do nums1 = nums2 here because this operation is merely making nums1 point at nums2, and the initial nums1 memory block remains the same. Since the program only looks at the initial nums1 memory block, so this operation would give wrong results. nums1[:] = nums2[:] on the other hand copies the values from nums2 to nums1
            return 
        
        if n == 0:
            nums1 = nums1[:m]
            return


        p1 = m - 1
        p2 = n - 1
        curr = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[curr] = nums1[p1]
                p1 -= 1
            else:
                nums1[curr] = nums2[p2]
                p2 -= 1
            curr -= 1
        
        # only check there are any more elements left in p2, cz having them in p1 means they are at the right place
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]
```
