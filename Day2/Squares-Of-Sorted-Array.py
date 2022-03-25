class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mid = 0
        n = len(nums)
        
        while mid < n and nums[mid] < 0:
            mid += 1
        
        i = mid - 1
        j = mid
        
        ans = []
        
        while i >= 0 and j < n:
            if abs(nums[i]) < nums[j]:
                ans.append(nums[i]*nums[i])
                i -= 1
            else:
                ans.append(nums[j]*nums[j])
                j += 1
        
        while i >= 0:
            ans.append(nums[i]*nums[i])
            i -= 1
        
        while j < n:
            ans.append(nums[j]*nums[j])
            j += 1
        
        
        return ans
            
