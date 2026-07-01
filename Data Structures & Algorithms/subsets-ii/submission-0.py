class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # [1,1,2]
        ans = [] 

        def backtracking(i, path):
            if i == len(nums):
                if path not in ans:
                    ans.append(path[:])
                return 


            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                # include
                path.append(nums[j])
                backtracking(j + 1, path)
                path.pop()
                # exclude
                backtracking(j + 1, path)

        backtracking(0, [])

        return ans