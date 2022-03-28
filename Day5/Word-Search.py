class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            
            if i < 0 or i == n or j < 0 or j == m or board[i][j] == "." or board[i][j] != word[idx]:
                return False
            
            char = board[i][j]
            board[i][j] = "."
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for x, y in directions:
                if dfs(i + x, j + y, idx + 1):
                    return True
            
            board[i][j] = char
            return False
        
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        
        return False
