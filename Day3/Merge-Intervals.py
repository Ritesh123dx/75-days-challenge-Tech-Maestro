class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort()
        ans = [intervals[0]]
        n = len(intervals)
        
        for i in range(1, n):
            start, end = intervals[i]
            
            if ans[-1][1] >= start:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])
        
        return ans
