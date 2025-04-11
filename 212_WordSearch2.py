'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        if not board or not board[0] or not words:
            return []

        #Build the trie with all words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
            node.word = word

        m,n = len(board), len(board[0])
        result = []

        def dfs(row, col, node):
            # Base Case
            if (row < 0 or row >= m or col < 0 or col >= n or board[row][col] == '#' or board[row][col] not in node.children):
                return
            
            char = board[row][col]
            curr_node = node.children[char]

            if curr_node.is_end_of_word:
                result.append(curr_node.word)
                '''By setting is_end_of_word = False after finding the word once, we ensure that even if we encounter the same word again during our search, we won't add it to our results multiple times.'''
                curr_node.is_end_of_word = False

             # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Explore all four directions
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in directions:
                dfs(row+dr, col+dc, curr_node)

            #Restore the cell
            board[row][col] = temp

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return result


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None
