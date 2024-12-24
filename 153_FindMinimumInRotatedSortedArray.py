'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        #One of the base cases where length of list is 0.
        if len(nums) == 1:
            return nums[0]
        #Already sorted array having no rotation will have this case for sure.
        if nums[0] < nums[-1]:
            return nums[0]
        while l < r:
            m = (l + r) // 2
            #If mid part is greater than mid+1 part then mid+1 must be smallest.
            if nums[m] > nums[m+1]:
                return nums[m+1]
            #IF mid is greater than leftmost element then smallest must be in second half
            elif nums[m] > nums[l]:
               l = m
            #otherwise in first half.
            else:
                r = m
        return nums[-1]

        
