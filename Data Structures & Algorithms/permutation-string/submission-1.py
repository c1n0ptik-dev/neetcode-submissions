class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        map1 = {}
        map2 = {}

        for i in s1:
            map1[i] = map1.get(i, 0) + 1

        for k in range(n1):
            letter = s2[k]
            map2[letter] = map2.get(letter, 0) + 1

        for right in range(n1, n2):
            if map1 == map2:
                return True
            map2[s2[right - n1]] -= 1
            if map2[s2[right - n1]] == 0:
                del map2[s2[right - n1]]
                
            map2[s2[right]] = map2.get(s2[right], 0) + 1


        return map1 == map2
