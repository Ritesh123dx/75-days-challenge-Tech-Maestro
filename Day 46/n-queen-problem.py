class Solution:
    def nQueen(self, n):
        # code here
        
        def isValid(row_no, col_no, cols):
            for r in range(1, len(cols) + 1):
                if cols[r - 1] == col_no:
                    return False
                
                if row_no - r == abs(col_no - cols[r - 1]):
                    return False
            
            return True
        
        def solve(row_no, cols, n):
            if row_no == n + 1:
                # print(cols)
                ans.append(cols[:])
                return
            
            for col_no in range(1, n + 1):
                if isValid(row_no, col_no, cols):
                    cols.append(col_no)
                    solve(row_no + 1, cols, n)
                    cols.pop()
            
        
        cols = []
        ans = []
        solve(1, cols, n)
        
        return ans


