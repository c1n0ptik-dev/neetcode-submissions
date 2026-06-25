class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_m, h_m = 0, len(matrix) - 1

        while l_m <= h_m:
            mid_m = l_m + (h_m - l_m) // 2


            if matrix[mid_m][0] > target:
                h_m = mid_m - 1

            elif matrix[mid_m][-1] < target:
                l_m = mid_m + 1

            else:
                l, h = 0, len(matrix[mid_m]) - 1

                while l <= h:
                    mid = l + (h - l) // 2

                    guess = matrix[mid_m][mid]

                    if target > guess:
                        l = mid + 1
                    
                    elif target < guess:
                        h = mid - 1

                    else:
                        return True
                
                return False

        return False
            

