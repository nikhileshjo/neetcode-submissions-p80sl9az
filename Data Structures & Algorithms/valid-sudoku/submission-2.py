class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                if num in seen:
                    if i in seen[num][0] or j in seen[num][1] or ((i//3)*3)+(j//3) in seen[num][2]:
                        return False
                    else:
                        seen[num][0] += (i,)
                        seen[num][1] += (j,)
                        seen[num][2] += ((i//3)*3+(j//3),)
                else:
                    seen[num] = [(i,), (j,), (((i//3)*3)+(j//3),)]
            
        return True