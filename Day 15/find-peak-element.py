class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[n - 2] < nums[n - 1]:
            return n - 1
        
        
        l = 0
        r = n - 1
        
        while l <= r:
            mid = (l + r)//2
            
            if mid == 0:
                l = mid + 1
                continue
            
            leftVal, rightVal = nums[mid - 1], nums[mid + 1]
            
            if leftVal < nums[mid] and nums[mid] > rightVal:
                return mid
            
            if leftVal < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            

