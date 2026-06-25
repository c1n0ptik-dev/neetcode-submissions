class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # min (height[i] + height[j]) * j - i 
        max_h = 0
        l, r = 0, len(heights) - 1

        while l < r:
            k = min(heights[l], heights[r]) * (r - l) 
            if k > max_h:
                max_h = k
            
            elif heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1
        
        return max_h
        

        