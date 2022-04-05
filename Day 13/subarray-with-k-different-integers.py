class Solution:
    
    def subArrayAtMost(self, nums, k):
        n = len(nums)
        hashmap = defaultdict(int)
        
        i, j = 0, 0
        ans = 0
        
        while j < n:
            hashmap[nums[j]] += 1
            
            if hashmap[nums[j]] == 1:
                k -= 1
                
            while k < 0:
                hashmap[nums[i]] -= 1
                if hashmap[nums[i]] == 0:
                    k += 1
                
                i += 1
            
            ans += j - i + 1
            j += 1
        
        
        return ans
    
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        return self.subArrayAtMost(nums, k) - self.subArrayAtMost(nums, k - 1)
