class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        prefix = [0]*n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        suffixSum = 0
        for i in range(n - 1, -1, -1):
            if suffixSum == prefix[i]:
                return i
            
            suffixSum += nums[i]
            
        
        return -1
