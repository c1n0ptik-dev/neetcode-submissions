class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(i, r, c, visited):
            if (r < 0 or len(board) <= r):
                return False

            if (c < 0 or len(board[r]) <= c):
                return False

            if i == len(word):
                return True
            
            if (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))

            found = (backtracking(i + 1, r, c, visited)
            or backtracking(i + 1, r + 1, c,  visited) 
            or backtracking(i + 1, r - 1, c, visited) 
            or backtracking(i + 1, r, c + 1, visited) 
            or backtracking(i + 1, r, c - 1, visited))

            visited.remove((r,c))
            return found
   
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (backtracking(0, i, j, set())):
                    return True

        return False
                