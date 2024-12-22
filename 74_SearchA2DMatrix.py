'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        
        
        end = len(matrix)-1
        mid = (start+end)//2

        while start <= end and target not in matrix[mid]:
            if target < matrix[mid][0]:
                end -= 1
            else:
                start += 1
            
            mid = (start+end)//2
        
        if target in matrix[mid]:
            return True
        else:
            return False
