class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, h = 0, len(nums) - 1

        while l <= h:
            mid = l + (h - l) // 2  
            guess = nums[mid]

            if guess > nums[h]:
                l = mid + 1
            
            elif guess < nums[h]:
                h = mid
            else:
                return guess

            

            

            