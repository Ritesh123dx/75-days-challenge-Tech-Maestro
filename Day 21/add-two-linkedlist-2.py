# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1 = []
        while l1 != None:
            stack1.append(l1.val)
            l1 = l1.next
        
        stack2 = []
        while l2 != None:
            stack2.append(l2.val)
            l2 = l2.next
        
        
        
        
        ptr = None
        carry = 0
        while len(stack1) > 0 and len(stack2) > 0:
            s = stack1.pop() + stack2.pop() + carry
            node = ListNode(s%10)
            
            if ptr == None:
                ptr = node
            else:
                node.next = ptr
                ptr = node
            
            carry = s//10
            
        
        while len(stack1) > 0:
            s = stack1.pop() + carry
            node = ListNode(s%10)
            if ptr == None:
                ptr = node
            else:
                node.next = ptr
                ptr = node
            
            carry = s//10
        
        while len(stack2) > 0:
            s = stack2.pop() + carry
            node = ListNode(s%10)
            if ptr == None:
                ptr = node
            else:
                node.next = ptr
                ptr = node
            
            carry = s//10
        
        
        if carry > 0:
            node = ListNode(carry)
            node.next = ptr
            ptr = node
            
        
        return ptr
            
            
            
            
            
            
        
