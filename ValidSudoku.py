'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in  range(9)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]


                if curr == '.':
                    continue
                
                box_index = (i//3) * 3 + j//3

                if (curr in row[i] or 
                    curr in col[j] or
                    curr in boxes[box_index]):
                    return False

                row[i].add(curr)
                col[j].add(curr)
                boxes[box_index].add(curr)
            
        return True
        
