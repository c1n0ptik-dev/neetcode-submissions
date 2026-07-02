class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        def backtracking(i, path):
            ans.append(path[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                backtracking(j + 1, path)
                path.pop()

        backtracking(0, [])

        return ans 
        
