class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        hashmap = defaultdict(int)
        count = 0
        
        for i in range(n):
            x = time[i]
            
            if x%60 == 0:
                count += hashmap[0]
                hashmap[0] += 1
            else:
                count += hashmap[60 - x%60]
                hashmap[x%60] += 1
        
        
        
        return count
