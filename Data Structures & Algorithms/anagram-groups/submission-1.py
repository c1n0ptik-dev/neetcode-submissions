class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str not in hashMap:
                hashMap[sorted_str] = [i]
            else:
                hashMap[sorted_str].append(i)
        
        return [i for i in hashMap.values()]

        
