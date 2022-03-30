class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return 0
        
        currJumps = nums[0]
        maxJumps = nums[0]
        count = 1
        
        
        for i in range(1, n - 1):
            currJumps -= 1
            maxJumps -= 1
            
            maxJumps = max(maxJumps, nums[i])
            
            if currJumps == 0:
                currJumps = maxJumps
                count += 1
            
        
        return count
        
        
