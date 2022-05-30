class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashmap = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000
        }
      
        num = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == 'I' or s[i] == "X" or s[i] == "C":
                if i + 1 < n and s[i] + s[i + 1] in hashmap:
                    num += hashmap[s[i] + s[i + 1]]
                    i += 2
                else:
                    num += hashmap[s[i]]
                    i += 1
            
            else:
                num += hashmap[s[i]]
                i += 1
        
        return num
                
