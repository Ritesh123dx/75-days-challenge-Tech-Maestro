"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root == None:
            return None
        
        start_ptr = root
        
        while start_ptr.left != None:
            
            parent = start_ptr
            
            while parent != None:
                left_child = parent.left
                right_child = parent.right
                
                left_child.next = right_child
                
                if parent.next:
                    right_child.next = parent.next.left
                
                parent = parent.next
            
            start_ptr = start_ptr.left
        
        
        return root
            
