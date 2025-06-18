'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word or not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        def backtrack(row, col, index):

            #Base Case: Found the word
            if len(word) == index:
                return True
            
            #Check bounds and character match.
            if (row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]):
                return False
            
            #Mark current cell is visited
            temp = board[row][col]
            board[row][col] = '#'

            #Explore all 4 directions
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            found = False

            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if backtrack(newRow, newCol, index+1):
                    found = True
                    break
            
            #Restore original board
            board[row][col] = temp
            return found
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
    
        return False
        
