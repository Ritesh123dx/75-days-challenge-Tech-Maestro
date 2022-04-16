class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n = len(nums2)
        nge = [-1]*n
        stack = []
        
        
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and nums2[i] >= stack[-1]:
                stack.pop()
            
            if len(stack) > 0:
                nge[i] = stack[-1]
            
            stack.append(nums2[i])
        
        hashmap = {}
        for i in range(n):
            hashmap[nums2[i]] = nge[i]
        
        ans = []
        for val in nums1:
            ans.append(hashmap[val])
        
        return ans
