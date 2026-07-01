class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []

        def backtracking(i, path, total):
            if total == target:
                ans.append(path[:])
                return
            if total > target or i >= len(candidates):
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                path.append(candidates[j])
                backtracking(j + 1, path, total + candidates[j])
                path.pop()

        backtracking(0, [], 0)
        return ans