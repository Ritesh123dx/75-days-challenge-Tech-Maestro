# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        ptr2 = dummy
        ptr1 = head
        
        while ptr1 != None:
            ptr1 = ptr1.next
            n -= 1
            
            if n < 0:
                ptr2 = ptr2.next
        
        
        ptr2.next = ptr2.next.next
        
        return dummy.next
            
        

