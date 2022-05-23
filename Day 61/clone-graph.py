"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def helper(self, node):
        if node == None:
            return None
        
        hashmap = {}
        newNode = Node(node.val)
        hashmap[newNode.val] = newNode
        
        queue = deque()
        queue.append(node)
        
        
        while len(queue):
            originalNode = queue.popleft()
            
            copiedNode = hashmap[originalNode.val]
            
            for neighbour in originalNode.neighbors:
                if neighbour.val not in hashmap:
                    copiedNeighbour = Node(neighbour.val)
                    hashmap[copiedNeighbour.val] = copiedNeighbour
                    queue.append(neighbour)
                    
                copiedNode.neighbors.append(hashmap[neighbour.val])
        
        
        return hashmap[node.val]
                
        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        clonedNode = self.helper(node)
        
        return clonedNode