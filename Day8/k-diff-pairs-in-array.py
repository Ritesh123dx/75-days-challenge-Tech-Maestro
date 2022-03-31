class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        hashmap = {}
        for val in nums:
            if val not in hashmap:
                hashmap[val] = 1
            else:
                hashmap[val] += 1
        
        
        ans = 0
        
        for val in hashmap.keys():
            if k == 0:
                n = hashmap[val]
                if n > 1:
                    ans += 1
            
            else:
                if val + k in hashmap:
                    ans += 1
        
        
        return ans
                
