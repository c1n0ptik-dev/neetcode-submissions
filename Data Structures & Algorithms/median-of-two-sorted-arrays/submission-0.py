class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            k = (l + r) // 2 # A
            j = half - k - 2 # B

            Aleft = A[k] if k >= 0 else float('-inf')
            Aright = A[k + 1] if k + 1 < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Bright, Aright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            if Aleft > Bright:
                r = k - 1

            else:
                l = k + 1

        
