class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(i, path):
            if i == len(nums):
                ans.append(path[:])
                return

            # Save the current
            path.append(nums[i])
            backtracking(i + 1, path)
            path.pop()

            # Move to the next one
            backtracking(i + 1, path)

        backtracking(0, [])

        return ans