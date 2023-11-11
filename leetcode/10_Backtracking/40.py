class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(candidates, target, path):
            if target == 0:
                res.append(path)
                return 
            if target < 0:
                return

            for i in range(len(candidates)): #
                if i > 0 and candidates[i] == candidates[i-1]: # skip duplicates
                    continue 
                backtrack(candidates[i+1:], target-candidates[i], path+[candidates[i]]) # candidates[i+1:] to avoid duplicates

        backtrack(candidates, target, [])
        return res

        
