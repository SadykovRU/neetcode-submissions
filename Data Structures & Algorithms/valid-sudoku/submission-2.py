class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check validity of input
        if len(board) != 9 or len(board[0]) != 9:
            return False
        
        visited = set()
        for i in range(9):
            for j in range(9):
                row, col = i // 3, j // 3
                if board[i][j] == ".":
                    continue
                elif (row, col, board[i][j]) not in visited and ("row", i, board[i][j]) not in visited and ("col", j, board[i][j]) not in visited:
                    visited.add((row, col, board[i][j]))
                    visited.add(("row", i, board[i][j]))
                    visited.add(("col", j, board[i][j]))
                else:
                     return False
        return True
        