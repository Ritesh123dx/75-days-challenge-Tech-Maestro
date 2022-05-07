class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def generate(start_idx, nums, temp, k):
            if len(temp) == k:
                ans.append(temp[:])
                return
            
            for i in range(start_idx, len(nums), 1):
                temp.append(nums[i])
                generate(i + 1, nums, temp, k)
                temp.pop()
            
        
        nums = [i for i in range(1, n + 1)]
        
        ans = []
        generate(0, nums, [], k)
        
        return ans
