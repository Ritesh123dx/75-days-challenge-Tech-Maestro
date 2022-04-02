class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = 10**8
        ans = -1
        
        for i in range(n - 2):
            a = nums[i]
            l = i + 1
            r = n - 1
            
            while l < r:
                b = nums[l]
                c =  nums[r]
                
                s = a + b + c
                
                if abs(s - target) < diff:
                    ans = s
                    diff = abs(s - target)
                
                if s > target:
                    r -= 1
                else:
                    l += 1
        
        return ans
                
