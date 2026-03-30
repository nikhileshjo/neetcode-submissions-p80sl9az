class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                for k in range(9):
                    if board[i][k] == board[i][j] and k != j:
                        return False
                for k in range(9):
                    if board[k][j] == board[i][j] and k != i:
                        return False
                for l in range((i//3)*3, ((i//3)*3)+3):
                    for m in range((j//3)*3, ((j//3)*3)+3):
                        if board[l][m] == board[i][j] and (l,m) != (i,j):
                            return False
            
        return True