class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # [1,1,2]
        ans = [] 

        def backtracking(i, path):
            if i == len(nums):
                if path not in ans:
                    ans.append(path[:])
                return 


            path.append(nums[i])
            backtracking(i + 1, path)
            path.pop()
            # exclude

            while i + 1 < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i + 1, path)
               

        backtracking(0, [])

        return ans