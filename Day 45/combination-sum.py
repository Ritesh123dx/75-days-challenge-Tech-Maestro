class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def generate(start_idx, candidates, ans_set, target):
            if target == 0:
                final_ans.append(ans_set[:])
                return
            
            for i in range(start_idx, len(candidates)):
                if candidates[i] <= target:
                    ans_set.append(candidates[i])
                    generate(i, candidates, ans_set, target - candidates[i])
                    ans_set.pop()
            
        
        
        final_ans = []
        generate(0, candidates, [], target)
        
        return final_ans
