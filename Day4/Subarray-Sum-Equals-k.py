class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        count = 0
        hashmap = defaultdict(lambda : 0)
        hashmap[0] = 1
        s = 0
        
        
        for i in range(n):
            s += nums[i]
            
            if s - k in hashmap:
                count += hashmap[s - k]
            
            hashmap[s] += 1
        
        
        
        return count
    
  
