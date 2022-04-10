class Solution:
    
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def mergesort(l, r):
            if l < r:
                mid = (l + r)//2
                mergesort(l, mid)
                mergesort(mid + 1, r)
                merge(l, mid, r)
        
        def merge(l, mid, r):
            i = l
            j = mid + 1
            cnt = 0
            
            temp = []
            
            while i <= mid and j <= r:
                if nums[j][0] < nums[i][0]:
                    cnt += 1
                    temp.append(nums[j])
                    j += 1
                else:
                    index = nums[i][1]
                    ans[index] += cnt
                    temp.append(nums[i])
                    i += 1
            
            while i <= mid:
                temp.append(nums[i])
                ans[nums[i][1]] += cnt
                i += 1
            
            while j <= r:
                temp.append(nums[j])
                j += 1
            
            
            temp_index = 0
            for i in range(l, r + 1):
                nums[i] = temp[temp_index]
                temp_index += 1
            
            
        
        n = len(nums)
        for i in range(n):
            val = nums[i]
            nums[i] = (val, i)
            
        ans = [0]*n
        mergesort(0, n - 1)
        
        return ans
        
        
