class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        
        arr = set(nums)

        largest_seq = 0

        for num in arr:
            curr_seq = 1
            if num - 1 not in arr:
                current_num = num
                while current_num + 1 in arr:
                    current_num += 1
                    curr_seq += 1

                largest_seq = max(curr_seq, largest_seq)

        return largest_seq