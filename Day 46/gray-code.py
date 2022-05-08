class Solution:
    
    def grayCode(self, n: int) -> List[int]:
        
        ans = ['0', '1']
        
        count = 1
        
        while count < n:
            temp = []
            
            for i in range(len(ans)):
                temp.append('0' + ans[i])
            
            for i in range(len(ans) - 1, -1, -1):
                temp.append('1' + ans[i])
            
            
            ans = temp[:]
            count += 1
        
        
        for i in range(len(ans)):
            ans[i] = int(ans[i], 2)
        
        return ans
