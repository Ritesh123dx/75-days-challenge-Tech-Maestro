class Node:
    def __init__(self, val : int):
        self.val = val
        self.rank = 1
        self.parent = val

class DSU:
    def __init__(self):
        self.map = {}  #element -> set
    
    def addElement(self, val : int) -> None:
        if val not in self.map:
            self.map[val] = Node(val)
    
    def findParent(self, val : int) -> int:
        node = self.map[val]
        
        if node.parent == node.val:
            return node.val
        
        node.parent = self.findParent(node.parent)
        
        return node.parent
    
    
    def union(self, val1 : int, val2: int) -> None:
        
        parent1 = self.findParent(val1)
        parent2 = self.findParent(val2)
        
        node1 = self.map[parent1]
        node2 = self.map[parent2]
     
        if node1.rank > node2.rank:
            node2.parent = node1.val
        elif node1.rank < node2.rank:
            node1.parent = node2.val

        else:
            node1.rank += 1
            node2.parent = node1.val
            
    
    def isSameSet(self, val1 : int, val2 : int) -> bool:
        parent1 = self.findParent(val1)
        parent2 = self.findParent(val2)
        
        return parent1 == parent2
        
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        dsu = DSU()
        
        for x, y in edges:
            dsu.addElement(x)
            dsu.addElement(y)
            
            if dsu.isSameSet(x, y):
                return [x, y]
            
            dsu.union(x, y)
        