import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def min_time_calc(speed):
            return sum(math.ceil(i / speed) for i in piles)
        
        max_r = max(piles)
        l, t = 1, max_r
        min_time = max_r

        while l <= t:
            mid = l + (t - l) // 2

            if min_time_calc(mid) <= h:
                min_time = mid
                t = mid - 1
            
            else:
                l = mid + 1
                

        return min_time
            
        
            



        