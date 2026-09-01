class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Input check
        if len(board[0]) != 9 or len(board) != 9:
            return False
        
        # Check all three constraints at the same time
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                digit = board[i][j]
                box = (i//3, j//3)

                if (i, digit) in seen or (digit, j) in seen or (box, digit) in seen:
                    return False
                
                seen.add((i, digit))
                seen.add((digit, j))
                seen.add((box, digit))
        
        return True
        