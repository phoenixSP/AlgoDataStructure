# Leetcode 217: https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Use set to keep track of nums
        TC: O(n)
        SC: O(n)
        '''
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False
