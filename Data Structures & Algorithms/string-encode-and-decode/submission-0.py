class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += f'{len(i)}#{i}'
        
        return s

    def decode(self, s: str) -> List[str]:
        arr = []
        num = '' 
        i = 0
        while i < len(s):
            if s[i] == "#":
                word = s[i + 1:i + 1 + int(num)]
                arr.append(word)
                i += 1 + len(word)
                num = ''
                continue
            elif s[i].isnumeric():
                num += s[i]
            
            i += 1

        return arr
                


