# Leetcode #: 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Solution: 
        - Create a hashmap of counts while iterating over the list O(n)
        - while adding/updating the count in hashmap, keep note of maxcount seen till now
        TC: O(n), SC: O(n)
        '''

        # hashmap = {}
        # max_count = 0
        # res = None

        # for n in nums:
        #     if n not in hashmap:
        #         hashmap[n] = 0
        #     hashmap[n] += 1

        #     if max_count < hashmap[n]:
        #         res = n
        #         max_count = hashmap[n]

        # return res

        '''
        Optimal solution
        - Use count and res to keep track of majority element
        - If current_item = res, count += 1
        - if current_item ~=res, count -= 1
        - when count is 0 again, update res

        SOLUTION FOUND BY 

        TC: O(n)
        SC: O(1)
        '''

        res = None 
        count = 0

        for n in nums:
            if count == 0:
                res = n
            
            count += (1 if res == n else -1)
        
        return res
