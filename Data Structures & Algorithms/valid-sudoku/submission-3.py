class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Brute force
        col_sets = [set() for _ in range(9)]
        for i in range(9):
            row_set = set()
            if i%3 == 0:
                sub_box_sets = [set() for _ in range(3)]
            
            for j in range(9):
                ele = board[i][j]
                if ele == ".":
                    continue
                if ele in row_set or ele in col_sets[j] or ele in sub_box_sets[j//3]:
                    return False
                row_set.add(ele)
                col_sets[j].add(ele)
                sub_box_sets[j//3].add(ele)
        return True