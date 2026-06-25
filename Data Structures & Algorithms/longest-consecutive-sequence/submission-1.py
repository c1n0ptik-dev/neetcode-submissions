class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        arr = sorted(nums)
        largest_seq = 0
        curr_seq = 1

        for i in range(len(nums) - 1):
            
            if arr[i + 1] == arr[i] + 1:
                curr_seq += 1
                
            elif arr[i + 1] > arr[i] + 1:
                if curr_seq > largest_seq:
                    largest_seq = curr_seq

                curr_seq = 1


        return largest_seq if largest_seq > curr_seq else curr_seq