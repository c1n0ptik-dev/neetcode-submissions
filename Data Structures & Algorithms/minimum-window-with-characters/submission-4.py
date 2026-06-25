from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        lettersS, lettersT = {}, {}

        for i in t:
            lettersT[i] = lettersT.get(i, 0) + 1

        have = 0
        needed = len(lettersT)
        ans, ansLen = [0, 0], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            lettersS[c] = lettersS.get(c, 0) + 1

            if c in lettersT and lettersS[c] == lettersT[c]:
                have += 1
            
            while have == needed:
                if r - l + 1 < ansLen:
                    ans = [l, r]
                    ansLen = r - l + 1
                
                lettersS[s[l]] -= 1

                if s[l] in lettersT and lettersS[s[l]] < lettersT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = ans

        return s[l:r + 1] if ansLen != float('inf') else ""
