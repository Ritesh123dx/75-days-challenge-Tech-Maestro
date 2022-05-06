class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isValid(num, row, col, rows_set, cols_set):
            if num in rows_set[row] or num in cols_set[col]:
                return False
            
            start_row_idx = 3*(row//3)
            start_col_idx = 3*(col//3)
            
            for i in range(start_row_idx, start_row_idx + 3):
                for j in range(start_col_idx, start_col_idx + 3):
                    if board[i][j] == num:
                        return False
            
            return True
                    
        
        n = 9
        rows_set = []
        cols_set = []
        for i in range(n):
            rows_set.append(set())
            cols_set.append(set())
        
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    rows_set[i].add(board[i][j])
                    cols_set[j].add(board[i][j])
        
        
        def backtrack(row, col, board, rows_set, cols_set):
            if row == 9 and col == 0:
                return True
            
            if col == 9:
                return backtrack(row + 1, 0, board, rows_set, cols_set)
            
            if board[row][col] != ".":
                return backtrack(row, col + 1, board, rows_set, cols_set)
            
            
            for num in "123456789":
                if isValid(num, row, col, rows_set, cols_set):
                    board[row][col] = num
                    rows_set[row].add(num)
                    cols_set[col].add(num)
                
                    if backtrack(row, col + 1, board, rows_set, cols_set):
                        return True
                    
                    board[row][col] = "."
                    rows_set[row].remove(num)
                    cols_set[col].remove(num)
            
            
            return False
        
        
        if backtrack(0, 0, board, rows_set, cols_set):
            return board
            
            