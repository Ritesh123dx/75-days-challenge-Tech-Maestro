class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs1(nums, target):
            l = 0
            r = len(nums) - 1
            index = -1
            
            while l <= r:
                mid = (l + r)//2
                
                if nums[mid] == target:
                    index = mid
                    r = mid - 1
                
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return index
        
        def bs2(nums, target):
            l = 0
            r = len(nums) - 1
            index = -1
            
            while l <= r:
                mid = (l + r)//2
                
                if nums[mid] == target:
                    l = mid + 1
                    index = mid
                
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return index
        
        
        index1 = bs1(nums, target)
        index2 = bs2(nums, target)
        
        return [index1, index2]
            

        
        
