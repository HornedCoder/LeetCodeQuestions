'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This stack stores (index, height) pair.
        stack = []
        maxArea = 0
        #Why? Because we are adding 0 to check 
        #for the rest of elements.
        #Our main process happens in while loop.
        #To make this algo work we need 0 at the end.
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                #Checks for previous bar
                index, height = stack.pop()
                #This while loop works in a way
                #like it takes a bar and checks maxArea of that bar.
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
        return maxArea
