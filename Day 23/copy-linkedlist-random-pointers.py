"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None
        
    
        ptr = head
        
        while ptr != None:
            copy = Node(ptr.val)
            next_node = ptr.next
            ptr.next = copy
            copy.next = next_node
            
            ptr = next_node
        
        
        ptr = head
        
        while ptr != None:
            if ptr.random != None:
                copy = ptr.next
                copy.random = ptr.random.next
            
            ptr = ptr.next.next
        
        
        copy_head = head.next
        
        ptr = head
        
        while ptr != None:
            copy = ptr.next
            next_node = ptr.next.next
            
            ptr.next = next_node
            
            if next_node != None:
                copy.next = next_node.next
                
            ptr = next_node
        
        
        return copy_head
        
        
