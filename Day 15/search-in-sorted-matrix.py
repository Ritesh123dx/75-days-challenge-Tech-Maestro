class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n, m = len(matrix), len(matrix[0])
        l = 0
        r = n*m - 1
      
        while l <= r:
            mid = (l + r)//2
            
            if matrix[mid//m][mid%m] == target:
                return True
            
            if matrix[mid//m][mid%m] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        
        return False
        
