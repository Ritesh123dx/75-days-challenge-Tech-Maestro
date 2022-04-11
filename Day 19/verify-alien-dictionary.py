class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i in range(len(order)):
            hashmap[order[i]] = i
        
        
        def compare(word1, word2):
            n, m = len(word1), len(word2)
            
            i, j = 0, 0
            
            while i < n and j < m:
                char1 = word1[i]
                char2 = word2[j]
                
                if hashmap[char1] > hashmap[char2]:
                    return False
                
                elif hashmap[char1] < hashmap[char2]:
                    return True
                
                else:
                    i += 1
                    j += 1
                    
            
            return i == n
            
        
        
        n = len(words)
        
        for i in range(1, n):
            if compare(words[i - 1], words[i]) == False:
                return False
        
        return True
