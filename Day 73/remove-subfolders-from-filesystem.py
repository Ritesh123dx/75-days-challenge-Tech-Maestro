class Node:
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.isWord = False
        self.word = ""

        
class Trie:
    def __init__(self):
        self.root = Node("-")
    
    
    def add(self, word):
        word_list = word.split("/")
        node = self.root
        
        for val in word_list:
            
            if node.next.get(val, None) == None:
                node.next[val] = Node(val)
            
            node = node.next[val]
        
        node.isWord = True
        node.word = word
    
    
    def getAns(self):
        ans = []
        
        self.helper(self.root, ans)
        
        return ans
    
    def helper(self, node, ans):
        if node == None:
            return
            
        if node.isWord:
            ans.append(node.word)
            return
        
        for key in node.next.keys():
            self.helper(node.next[key], ans)
            
                
            
        

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
    
        n = len(folder)
        trie = Trie()
        
        for directory in folder:
            trie.add(directory)
        
        
        return trie.getAns()
    
