class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        lis = [1]*n
        max_lis = 1
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    lis[j] = max(lis[j], 1 + lis[i])
                    max_lis = max(max_lis, lis[j])
        
        
        return max_lis

