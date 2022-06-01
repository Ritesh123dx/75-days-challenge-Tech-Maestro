class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getHash(string):
            freq = [0]*26
            for char in string:
                index = ord(char) - 97
                freq[index] += 1
            
            hashValue = ""
            for num in freq:
                hashValue += str(num) + "-"
            
            
            return hashValue
        
        hashmap = defaultdict(list)
        
        for string in strs:
            hashValue = getHash(string)
            hashmap[hashValue].append(string)
        
        
        ans = []
        for key in hashmap.keys():
            ans.append(hashmap[key])
        
        return ans
