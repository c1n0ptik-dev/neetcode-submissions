class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 

            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtracking(path)
                path.pop()

        
        backtracking([])

        return ans