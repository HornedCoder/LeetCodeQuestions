'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        sorted_freq = tuple(sorted(freq.items(), key = lambda x:x[1], reverse = True))
        for i in range(k):
            ans.append(sorted_freq[i][0])

        return ans
