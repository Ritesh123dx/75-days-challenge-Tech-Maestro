class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(capacity, days):
            count = 1
            s = 0
            for i in range(len(weights)):
                s += weights[i]
                if s > capacity:
                    count += 1
                    s = weights[i]
                
                if count > days:
                    return False
            
            return True
        
        
        lb = max(weights)
        ub = sum(weights)
        ans = 0
        
        while lb <= ub:
            capacity = (lb + ub)//2
            
            if check(capacity, days):
                ans = capacity
                ub = capacity - 1
            else:
                lb = capacity + 1
        
        
        return ans
