class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1

        while p1 != p2:
            num_l = numbers[p1]
            num_r = numbers[p2]

            if num_l + num_r > target:
                p2 -= 1
            
            elif num_l + num_r < target:
                p1 += 1
            
            else:
                return [p1 + 1, p2 + 1]
