# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseLinkedList(start, end):
            prev = None
            tail = start
            
            ptr = start
            while ptr != end:
                next_node = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = next_node
            
            return prev, tail
        
        
        if k == 1:
            return head
        
        
        dummy = ListNode(-1)
        dummy.next = head
        
        ptr = dummy
        
        while True:
            start_boundary = ptr
            count = 0
            
            while count < k and ptr != None:
                ptr = ptr.next
                count += 1
            
            if ptr == None:
                break
            
            end_boundary = ptr.next
            
            reversed_head, reversed_tail = reverseLinkedList(start_boundary.next, end_boundary)
            
            start_boundary.next = reversed_head
            reversed_tail.next = end_boundary
            
            ptr = reversed_tail
        
        
        
        return dummy.next
          
