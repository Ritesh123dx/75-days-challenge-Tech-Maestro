"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def helper(ptr):
            if ptr == None:
                return (None, None)
            
            head = ptr
            tail = None
            
            while ptr != None:
                if ptr.child:
                    child_head, child_tail = helper(ptr.child)
                    ptr.child = None
                    
                    child_tail.next = ptr.next
                    
                    if ptr.next:
                        ptr.next.prev = child_tail
                    
                    ptr.next = child_head
                    child_head.prev = ptr
                    
                    ptr = child_tail
                
                tail = ptr
                ptr = ptr.next
            
            
            return (head, tail)
        
        
        return helper(head)[0]
        
        
