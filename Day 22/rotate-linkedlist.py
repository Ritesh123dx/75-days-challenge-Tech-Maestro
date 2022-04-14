# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        length = 0
        ptr = head
        prev = None
        while ptr != None:
            prev = ptr
            ptr = ptr.next
            length += 1
            
        prev.next = head
        
        k = k%length
        k = length - k
        
        count = 1
        ptr = head
        while count < k:
            ptr = ptr.next
            count += 1
        
        new_head = ptr.next
        ptr.next = None
        
        return new_head
        
        
