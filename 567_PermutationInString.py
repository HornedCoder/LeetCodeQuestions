'''
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        
        window_freq = [0] * 26
        s1_freq = [0] * 26
        
        for i in s1:
            s1_freq[ord(i)-ord('a')] += 1
        
        for i in range(len(s1)):
            window_freq[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq == window_freq:
            return True

        for i in range(len(s1),len(s2)):
            window_freq[ord(s2[i - len(s1)]) - ord('a')] -= 1
            window_freq[ord(s2[i]) - ord('a')] += 1

            if s1_freq == window_freq:
                return True
        
        return False
