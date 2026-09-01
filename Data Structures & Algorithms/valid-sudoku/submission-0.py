class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Input check
        if len(board[0]) != 9 or len(board) != 9:
            return False
        
        # Check horizontal lines
        for line in board:
            visited = set()
            for digit in line:
                if digit == ".":
                    continue
                elif digit in visited:
                    return False
                else:
                    visited.add(digit)
        
        # Check vertical lines
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in visited:
                    return False
                else:
                    visited.add(board[j][i])
        
        # Check mini squares 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] == ".":
                            continue
                        elif board[i+k][j+l] in visited:
                            return False
                        else:
                            visited.add(board[i+k][j+l])
        
        return True
            