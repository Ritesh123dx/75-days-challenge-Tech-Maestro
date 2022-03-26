class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        pascal = [[1]]
        
        for n in range(2, numRows + 1):
            temp = [1]*(n)
            
            for i in range(1, n - 1):
                temp[i] = pascal[n - 2][i] + pascal[n - 2][i - 1]
            
            pascal.append(temp)
        
        
        return pascal
        
