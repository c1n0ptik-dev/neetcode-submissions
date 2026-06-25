class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        hashMap = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for i in s:
            if i in hashMap.keys():
                stack.append(hashMap[i])
            else:
                if not stack or stack.pop() != i:
                        return False
        
        return True if len(stack) == 0 else False
        