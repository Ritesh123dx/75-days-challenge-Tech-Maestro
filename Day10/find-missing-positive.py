class Solution:
    
    def partitionPositives(self, nums):
        n = len(nums)
        i, j = 0, 0
        
        while j < n:
            if nums[j] > 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            
            j += 1
        
        return i
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = self.partitionPositives(nums)
    
        
        for i in range(n):
            index = abs(nums[i]) - 1
            
            if index < n:
                nums[index] = -abs(nums[index])
        
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1
