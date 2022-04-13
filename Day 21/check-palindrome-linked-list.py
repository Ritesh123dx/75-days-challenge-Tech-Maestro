# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, ptr):
        prev = None
        
        while ptr != None:
            next_node = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_node
        
        return prev
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next == None:
            return True
        
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        ptr = self.reverse(slow.next)
        
        
        while ptr != None:
            if ptr.val != head.val:
                return False
            ptr = ptr.next
            head = head.next
        
        return True
