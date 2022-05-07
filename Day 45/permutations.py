class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        def solve(nums, temp):
            if len(nums) == 0:
                ans.append(temp)
                return
            
            for i in range(len(nums)):
                val = nums[i]
                new_temp = temp[:] + [val]
                new_nums = nums[:i] + nums[i+1:]
                solve(new_nums, new_temp)
        
        solve(nums, [])
        return ans


