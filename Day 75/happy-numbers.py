class Solution:
    def isHappy(self, n: int) -> bool:
        myset = set()
        def findsum(n):
            s = 0
            while n != 0:
                digit = n%10
                s += digit*digit
                n = n//10
            return s
        
        s = n
        while True:
            s = findsum(s)
            if s == 1:
                return True
            if s in myset:
                return False
            myset.add(s)