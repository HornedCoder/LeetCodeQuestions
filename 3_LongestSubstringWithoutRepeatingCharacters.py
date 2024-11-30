'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

#The following solution takes like O(N^2) TC
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        substringList = []
        n = len(s)
        for i in range(n-1):
            currSubString = set()
            currSubString.add(s[i])
            for j in range(i+1,n):
                if s[j] not in currSubString:
                    currSubString.add(s[j])
                else:
                    substringList.append(currSubString)
                    break
            substringList.append(currSubString)
        maxLen = 0
        for i in substringList:
            if len(i) > maxLen:
                maxLen = len(i)
        return maxLen
# We will try for more optimal TC in below code.
