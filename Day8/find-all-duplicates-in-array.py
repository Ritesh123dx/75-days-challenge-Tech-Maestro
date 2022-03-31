class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        duplicates = []
        n = len(nums)
        
        for i in range(n):
            index = abs(nums[i]) - 1
            
            if nums[index] < 0:
                duplicates.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        
        return duplicates
    
    '''
    
    [4, -3, -2, -7, 8, 2, 3, 1]
     0   1   2   3  4  5  6  7
    
    '''
