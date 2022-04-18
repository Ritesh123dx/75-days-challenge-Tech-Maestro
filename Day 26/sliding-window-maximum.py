class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        ans = []
        
        for i in range(len(nums)):
            while len(queue) > 0 and nums[i] > queue[-1]:
                queue.pop()
            
            queue.append(nums[i])
            
            if i < k - 1:
                i += 1
                continue
            
            ans.append(queue[0])
            
            if nums[i - k + 1] == queue[0]:
                queue.popleft()
            
            
        
        return ans
