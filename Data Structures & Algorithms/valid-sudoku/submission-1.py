class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s_1 = set()
            s_2 = set()

            for j in range(9):
                val_1 = board[i][j]
                val_2 = board[j][i]
                if val_1 not in s_1:
                    s_1.add(val_1)
                elif val_1 != '.' :
                    return False

                if val_2 not in s_2:
                    s_2.add(val_2)

                elif val_2 != '.':
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