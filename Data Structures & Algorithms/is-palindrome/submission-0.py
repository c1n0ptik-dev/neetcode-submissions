class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''.join(c.lower() for c in s if c.isalnum())
        p1, p2 = 0, len(k) - 1

        while p1 < p2:
            if k[p1] != k[p2]:
                return False
            
            p1 += 1
            p2 -= 1
        
        return True