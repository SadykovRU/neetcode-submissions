class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                box_row, box_col = i // 3, j // 3
                
                if (box_row, box_col, board[i][j]) in seen or (i, board[i][j]) in seen or (board[i][j], j) in seen:
                    return False
                else:
                    seen.add((box_row, box_col, board[i][j]))
                    seen.add((i, board[i][j]))
                    seen.add((board[i][j], j))
        return True
        