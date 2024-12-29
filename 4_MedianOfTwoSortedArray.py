'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newL = []
        i,j,k = 0,0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                newL.append(nums1[i])
                i+=1
            else:
                newL.append(nums2[j])
                j+=1
        while i < len(nums1):
            newL.append(nums1[i])
            i+=1
        while j < len(nums2):
            newL.append(nums2[j])
            j+=1
        
        if len(newL)%2==0:
            ans = (((newL[(len(newL))//2])+newL[(len(newL)//2)-1])/2)
        else:
            ans = newL[(len(newL)//2)]
        return ans
