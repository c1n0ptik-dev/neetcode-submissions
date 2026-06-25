class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashMap.keys():
                return [hashMap[target - nums[i]], i]
            
            hashMap[nums[i]] = i
