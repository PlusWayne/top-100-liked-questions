class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dp(sorted(candidates), target, 0, [], res)
        return res
        
    def dp(self, candidates, target, index, path, res):
        if target == 0:
            res.append(path)
        if target <= 0:
            return
        for i in range(index, len(candidates)):
            self.dp(candidates, target-candidates[i], i, path + [candidates[i]], res)
