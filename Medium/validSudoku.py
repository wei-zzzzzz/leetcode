'''
Valid Sudoku
2020_11_19
Time: O(n^2)
Space: O(n)
思考流程：
1.暴力法依序檢查是否違反
2.檢查橫列
3.檢查直行
4.檢查九宮格（3格跳躍）
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for R in board:
            row = set()
            for r in R:
                if r not in row:
                    row.add(r)
                else:
                    if r != '.':
                        return False 
            if row == ('.'):
                return False 
            
        for c in range(9):
            column = set()
            for k in range(9):
                if board[k][c] not in column:
                    column.add(board[k][c])
                else:
                    if board[k][c] !='.':
                        return False  
            if column == ('.'):
                return False
            
        for ni in range(0, 9 ,3):
            for nj in range(0, 9 ,3):
                nine = set()
                for i in range(ni, ni+3):
                    for j in range(nj,nj+3):
                        if board[i][j] not in nine:
                            nine.add(board[i][j])
                        else:
                            if board[i][j] !='.':
                                return False  
                if nine == ('.'):
                    return False

        return True
