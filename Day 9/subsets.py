class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(index, temp):
            ans.append(temp[:])
            
            for i in range(index, len(nums)):
                temp.append(nums[i])
                helper(i + 1, temp)
                temp.pop()
                
        
        ans = []
        helper(0, [])
        
        return ans
