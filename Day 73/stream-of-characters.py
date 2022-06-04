class Node:
    def __init__(self, character):
        self.characater = character
        self.next = [None]*26
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node("/")
        
    
    def add(self, word):
        node = self.root
        n = len(word)
        
        for i in range(n - 1, -1, -1):
            char = word[i]
            index = ord(char) - 97
            
            if node.next[index] == None:
                node.next[index] = Node(char)
            
            node = node.next[index]
        
        
        node.isWord = True
    
    
    def checkSuffix(self, word):
        n = len(word)
        node = self.root
        
        for i in range(n - 1, -1, -1):
            char = word[i]
            index = ord(char) - 97
            
            if node.next[index] == None:
                return False
            
            node = node.next[index]
            
            if node.isWord:
                return True
        
        return False
        

class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.trie = Trie()
        self.string = ""
        
        for word in words:
            self.trie.add(word)
        
    def query(self, letter: str) -> bool:
        
        self.string += letter
        
        return self.trie.checkSuffix(self.string)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
