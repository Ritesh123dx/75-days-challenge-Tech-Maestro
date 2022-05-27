class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 1
    
class DisjointSet:
    def __init__(self):
        self.hashmap = {}
        
    def addSet(self, key):
        if key not in self.hashmap:
            self.hashmap[key] = Node(key)
    
    
    def getParent(self, node):
        if node.parent == node:
            return node
        
        node.parent = self.getParent(node.parent)
        
        return node.parent
    
    def union(self, key1, key2):
        node1 = self.hashmap[key1]
        node2 = self.hashmap[key2]
        
        parent1 = self.getParent(node1)
        parent2 = self.getParent(node2)
        
        if parent1 != parent2:
            if parent1.rank > parent2.rank:
                parent2.parent = parent1
            elif parent1.rank < parent2.rank:
                parent1.parent = parent2
            else:
                parent1.rank += 1
                parent2.parent = parent1
    
    def isSameSet(self, key1, key2):
        node1 = self.hashmap[key1]
        node2 = self.hashmap[key2]
        
        parent1 = self.getParent(node1)
        parent2 = self.getParent(node2)
        
        return parent1 == parent2
        
        
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        DS = DisjointSet()
        
        for equation in equations:
            a, cmp1, cmp2, b = list(equation)
            
            if cmp1 == "=":
                DS.addSet(a)
                DS.addSet(b)
                DS.union(a, b)
        
        for equation in equations:
            a, cmp1, cmp2, b = list(equation)
            
            if cmp1 == "!":
                DS.addSet(a)
                DS.addSet(b)
                
                if DS.isSameSet(a, b):
                    return False
        
        
        return True
        
            
            
