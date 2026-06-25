class Solution:
    def trap(self, height: List[int]) -> int:

        nums = []

        pref = 0
        for i in height:
            if i > pref:
                pref = i
            nums.append(pref)

        suf = 0
        for k in range(len(height) -1, -1, -1):
            if height[k] > suf:
                suf = height[k]

            nums[k] = min(nums[k], suf)
            
        c = 0

        while c < len(height):
            nums[c] = nums[c] - height[c]
            c += 1

        return sum(nums)

