class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        def fun(dividend, divisor):
            
            ans = 0
            while dividend - divisor >= 0:
                
                temp = divisor
                count = 0
                
                while dividend - temp >= 0:
                    count += 1
                    temp = temp << 1
                
                temp = temp >> 1
                ans += 1 << (count - 1)
                
                dividend = dividend - temp
            
            
            return ans
        
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = 1
        
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        
        return sign*fun(abs(dividend), abs(divisor) )
                    
