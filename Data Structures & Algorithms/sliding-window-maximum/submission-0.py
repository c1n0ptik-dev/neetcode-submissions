from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        subarr = deque(nums[:k])
        ans.append(max(subarr))
        l = 0

        for r in range(k, len(nums)):
            subarr.popleft()
            subarr.append(nums[r])
            ans.append(max(subarr))
        
        return ans