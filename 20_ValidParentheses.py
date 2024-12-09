'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        dictParenClosed = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c not in dictParenClosed:
                stack.append(c)
                continue
            if not stack or dictParenClosed[c]!= stack[-1]:
                return False
            stack.pop()
        return not stack
