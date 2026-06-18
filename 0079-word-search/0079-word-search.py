class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n= len(board[0])
        def backtrack(row, col, i):
            if i == len(word):
                return True

            if row<0 or row >= m or col<0 or col >= n:
                return False

            if board[row][col] != word[i]:
                return False
            board[row][col] = '#'
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                
                if backtrack(row+dr, col+dc, i+1):
                    return True
                
            board[row][col] = word[i]
            return False
        for row in range(m):
            for col in range(n):
                if backtrack(row, col, 0):
                    return True
        return False