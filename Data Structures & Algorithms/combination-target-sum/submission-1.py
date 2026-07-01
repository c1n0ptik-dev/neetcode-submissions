class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking(i, path, total):
            if total == target:
                ans.append(path[:])
                return

            if i >= len(nums) or total > target:
                return 
            
            total += nums[i]
            path.append(nums[i])
            backtracking(i, path, total)
            total -= nums[i]
            path.pop()

            backtracking(i + 1, path, total)

        backtracking(0, [], 0)

        return ans