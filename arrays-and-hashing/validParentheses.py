class Solution:
    def isValid(self, s: str) -> bool:
        '''
        # Leetcode 20: https://leetcode.com/problems/valid-parentheses/
        
        Solution:
        - Iterate over the string s, create a stack (list) and a mapping with closing brackets as keys
        - If the current character is an opening bracket, add it to the stack
        - If the current character is a closing bracket, 
            - Return False if stack empty or stack top does not have same opening bracket
        - Return True if stack is empty

        TC: O(n)
        SC: O(n)
        '''

        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s: 
            if ch not in mapping: # opening bracket
                stack.append(ch)
            elif len(stack) == 0 or mapping[ch] != stack[-1]:
                return False
            else:
                stack.pop()

        return not stack
