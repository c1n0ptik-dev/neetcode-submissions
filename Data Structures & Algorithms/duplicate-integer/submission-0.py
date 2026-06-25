class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        for i in nums:
            if i in hashMap:
                return True
            hashMap.add(i)
        return False