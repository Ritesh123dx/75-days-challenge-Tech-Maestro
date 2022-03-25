class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums[0]
        votes = 1
        
        for i in range(1, n):
            if x == nums[i]:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    x = nums[i]
                    votes = 1
        
        return x
