'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 '''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #This will store output.
        answer = []
        #This will store index of potentially max elements.     
        window = collections.deque()    

        for i in range(len(nums)):
            #remove element which is outside the window.
            if window and window[0] <= i-k:
                window.popleft()
            #remove smaller elements from back of the window.
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            #Append new element.
            window.append(i)
            #Start adding answer as first window completes
            if i >= k-1:
                answer.append(nums[window[0]])
        
        return answer
