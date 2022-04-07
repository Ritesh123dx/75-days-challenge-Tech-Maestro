class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        sign = 1 if n > 0 else -1
        n = abs(n)
        
        const = 1
        prod = x
        
        while n > 1:
            if n%2 == 0:
                prod = prod*prod
                n = n//2
            else:
                const = const*prod
                n = n - 1
        
        
        if sign == 1:
            return const*prod
        else:
            return 1/(const*prod)
        
