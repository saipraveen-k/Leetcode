class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def backtrack(candidates, target, start, path, result):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(candidates, target - candidates[i], i, path + [candidates[i]], result)
        backtrack(candidates, target, 0, [], result)
        return result