class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def isValid(x):
            count = 0
            for val in nums:
                count += (val - 1)//x
                
                if count > maxOperations:
                    return False
            
            
            return True
        
        
        l = 1
        r = max(nums)
        ans = 0
        
        while l <= r:
            x = (l + r)//2
            
            if isValid(x):
                ans = x
                r = x - 1
            else:
                l = x + 1
        
        
        return ans
