class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()

            for j in range(9):
                val = board[i][j]
                if val not in s:
                    s.add(val)
                elif val != '.':
                    return False
            
        for i in range(9):
            s = set()

            for j in range(9):
                val = board[j][i]
                if val not in s:
                    s.add(val)
                elif val != '.':
                    return False
        
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6),
                ]
        for x, y in starts:
            s = set()

            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    val = board[i][j]
                    if val not in s:
                        s.add(val)
                    elif val != '.':
                        return False
        
        return True