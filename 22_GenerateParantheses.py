'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(openCount: int, closedCount: int, current: str):
            if len(current) == 2*n:
                result.append(current)
                return
            if openCount < n:
                backtrack(openCount+1, closedCount, current + '(')

            if closedCount < openCount:
                backtrack(openCount, closedCount+1, current+')')
        
        backtrack(0,0,"")
        return result
'''
The magic is in these two constraints:
pythonCopy# Only add open if we haven't used all n
if open_count < n:
    backtrack(open_count + 1, close_count, current + '(')

# Only add close if it won't break the balance
if close_count < open_count:
    backtrack(open_count, close_count + 1, current + ')')
These rules ensure we only generate valid parentheses combinations.
'''
