class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        
        hashmap = {0 : 2, 2 : 1}
        
        [2, 3, 2]  k = 5
        
        7%5 = 2
        
        
        count = 1 + 2
        '''
        
        hashmap = defaultdict(int)
        hashmap[0] = 1
        
        s = 0
        count = 0
        
        for val in nums:
            s += val
            
            target = (s%k + k)%k            
            count += hashmap[target]

            hashmap[target] += 1
                
            s = (s%k + k)%k
            
        return count
