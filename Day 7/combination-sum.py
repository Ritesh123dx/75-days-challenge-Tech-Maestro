class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def fun(idx, curr_sum, target, temp):
            if curr_sum == target:
                ans.append(temp[:])
                return
            
            if idx == len(nums):
                return
            
            for i in range(idx, len(nums)):
                if curr_sum + nums[i] <= target:
                    temp.append(nums[i])
                    fun(i, curr_sum + nums[i], target, temp)
                    temp.pop()
        
        
        ans = []
        fun(0, 0, target, [])
        
        return ans
        
        
        
