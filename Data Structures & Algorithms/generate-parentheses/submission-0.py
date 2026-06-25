class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []
        

        def backtrack(index, arr, n, opened, closed):
            if len(arr) == n:
                answers.append(''.join(arr[:]))
                return 
                    
            if opened < n // 2:
                backtrack(index + 1, arr + ["("], n, opened + 1, closed)
            if closed < opened:
                backtrack(index + 1, arr + [")"], n, opened, closed + 1)
        
        backtrack(0, [], n * 2, 0, 0)

        return answers
