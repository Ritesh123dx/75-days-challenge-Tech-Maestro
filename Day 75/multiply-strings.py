class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        n = len(num1)
        m = len(num2)
        arr = [""]*(n+m+1)
        
        k = 0
        for i in range(n - 1, -1, -1):
            s = 0
            carry = 0
            p = k
            for j in range(m - 1, -1, -1):
             
                if arr[p] == "":
                    arr[p] = "0"
                    
                s = int(num1[i])*int(num2[j]) + int(arr[p]) + carry
                
                carry = s//10
                s = s%10
                
                arr[p] = str(s)
                p += 1
            
            if carry:
                arr[p] = str(carry)
            
            k += 1
        
        ans = "".join(arr)
        
        return ans[::-1]
        
                