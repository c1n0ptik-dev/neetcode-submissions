from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        d = deque()

        for i in nums[:k]:
            while d and d[-1] < i:
                d.pop()
            d.append(i)
        
        ans.append(d[0])

        for p in range(k, n):
            if nums[p - k] == d[0]:
                d.popleft()
            
            while d and d[-1] < nums[p]:
                d.pop()

            d.append(nums[p])
            ans.append(d[0])

        return ans

        

                







        