'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(nums,target):
            left,right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
                
            return left
        def searchRight(nums,target):
            left,right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] <= target:
                    left = mid+1
                else:
                    right = mid-1
                
            return right
        
        L,R = searchLeft(nums,target), searchRight(nums,target)

        if L <= R and R <len(nums) and nums[L] == target:
            return [L,R]
        else:
            return[-1,-1]



