'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_for = [0] * n
        ans_rev = [0] * n
        ans = [0] * n
        for i in range(n):
            if i == 0:
                ans_for[i] = nums[i]
            else:
                ans_for[i] = nums[i]*ans_for[i-1]
                
        for i in range(n-1,-1,-1):
            if i == n-1:
                ans_rev[i] = nums[n-1]
            else:
                ans_rev[i] = nums[i] * ans_rev[i+1]
        
        for i in range(n):
            if i  == 0:
                ans[i] = ans_rev[i+1]
            elif i == n-1:
                ans[i] = ans_for[i-1]
            else:
                ans[i] = ans_rev[i+1] * ans_for[i-1]
        return ans
