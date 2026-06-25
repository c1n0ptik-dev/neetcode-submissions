class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        characters = {}
        longest = 0
        size = 0
        left = 0

        for right in range(n):
            characters[s[right]] = characters.get(s[right], 0) + 1

            while right - left + 1 - max(characters.values()) > k:
                characters[s[left]] = characters.get(s[left]) - 1
                left += 1
                

            size = right - left + 1
            longest = max(longest, size)

        return longest
            
            


            
            