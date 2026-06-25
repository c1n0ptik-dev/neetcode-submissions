class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
    
        res = [[] for _ in range(len(nums) + 1)]

        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for c, v in count.items():
            res[v].append(c)

        ans = []
        for i in range(len(res) - 1, 0, -1):
            for l in res[i]:
                ans.append(l)
                if len(ans) == k:
                    return ans
            

