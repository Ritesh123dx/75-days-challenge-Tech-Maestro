# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def getLen(head):
            count = 0
            while head != None:
                head = head.next
                count += 1
            
            return count
        
        n = getLen(headA)
        m = getLen(headB)
        
        
        while n != m:
            if n > m:
                headA = headA.next
                n -= 1
            else:
                headB = headB.next
                m -= 1
        
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
