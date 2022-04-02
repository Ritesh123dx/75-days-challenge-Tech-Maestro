class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        
        carry = 1
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            digit = digits[i]
            s = digit + carry
            carry = s//10
            ans.append(s%10)
        
        if carry:
            ans.append(carry)
            
        ans = ans[::-1]
        
        return ans
