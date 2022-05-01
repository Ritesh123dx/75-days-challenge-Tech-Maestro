# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        heapq.heapify(heap)
        n = len(lists)
        for i in range(n):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        
        dummy = ListNode(-1)
        ptr = dummy
        
        while len(heap) > 0:
            value, index, node = heapq.heappop(heap)
            
            ptr.next = node
            ptr = node
            
            if node.next != None:
                heapq.heappush(heap, (node.next.val, index, node.next) )
        
        
        return dummy.next
