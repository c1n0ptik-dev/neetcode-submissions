class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        options = ['(', ")"]
        ans = []

        def backtracking(l, r, path):
            if len(path) == n * 2:
                ans.append("".join(path[:]))
                return  

            if l > r:
                path.append(")")
                backtracking(l, r + 1, path)
                path.pop()

            if l < n:
                path.append("(")
                backtracking(l + 1, r, path)
                path.pop()
           

        backtracking(0, 0, [])
        return ans 



        