class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            guess = nums[mid]

            if guess > target:
                r = mid - 1
            
            elif guess < target:
                l = mid + 1
            
            else:
                return mid
        
        return -1

