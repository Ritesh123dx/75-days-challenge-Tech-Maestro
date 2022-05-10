class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        ans = nums[0]
        
        
        for i in range(1, len(nums)):
            tempMax = maxProd
            tempMin = minProd
            
            maxProd = max(nums[i], nums[i]*tempMax, nums[i]*tempMin)
            minProd = min(nums[i], nums[i]*tempMax, nums[i]*tempMin)
            
            ans = max(ans, maxProd)
            
            
        return ans
