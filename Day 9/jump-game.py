class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if nums[0] == 0 and n != 1:
            return False
        
        jumps = nums[0]
        
        for i in range(1, n - 1):
            jumps -= 1
            jumps = max(jumps, nums[i])
            
            if jumps == 0:
                return False
        
        return True
