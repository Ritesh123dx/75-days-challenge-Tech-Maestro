class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def check(mid):
            count = 1
            s = 0
            for i in range(len(nums)):
                s += nums[i]
                
                if s > mid:
                    s = nums[i]
                    count += 1
                
                if count > m:
                    return False
            
            return True
                
        
        l = max(nums)
        r = sum(nums)
        ans = 0
        
        while l <= r:
            mid = (l + r)//2
            
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        
        return ans
