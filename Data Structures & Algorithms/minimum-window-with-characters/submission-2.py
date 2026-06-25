from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        
        res = [0, 0]
        resLen = float('inf')

        if s_len < t_len:
            return ""

        countT = {}
        window = {}

        for i in t:
            countT[i] = countT.get(i, 0) + 1

        have = 0
        needed = len(countT)
        left = 0

        for right in range(s_len):
            c = s[right]
            window[c] = window.get(c, 0) + 1 

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == needed:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                k = s[left]

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""
            
