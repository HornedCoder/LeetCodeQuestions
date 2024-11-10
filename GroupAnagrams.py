'''
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = {}
            for char in s:
                count[char] = count.get(char, 0) + 1
            
            tup = tuple(sorted(count.items()))

            if tup in groups:
                groups[tup].append(s)
            else:
                groups[tup] = [s]
        return list(groups.values())
        
