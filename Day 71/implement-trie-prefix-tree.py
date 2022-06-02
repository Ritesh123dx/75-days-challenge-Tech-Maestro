class Node:
    
    def __init__(self, character, isWord = False):
        self.char = character
        self.isWord = isWord
        self.next = [None]*26

class Trie:

    def __init__(self):
        self.root = Node("/")
        

    def insert(self, word: str) -> None:
        node = self.root
        
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - 97
            
            if node.next[index] == None:
                node.next[index] = Node(char)
            
            node = node.next[index]
        
        node.isWord = True

    def search(self, word: str) -> bool:
        
        node = self.root
        
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - 97
            
            if node.next[index] == None:
                return False
            
            node = node.next[index]
        
        
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        
        for i in range(len(prefix)):
            char = prefix[i]
            index = ord(char) - 97
            
            if node.next[index] == None:
                return False
            
            node = node.next[index]
        
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
