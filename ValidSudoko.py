class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            s=set()
            for i in range(9):
                if board[row][i]==".":
                    continue
                if board[row][i] in s:
                    return False
                s.add(board[row][i])
        for col in range(9):
            s=set()
            for i in range(9):
                if board[i][col]==".":
                    continue
                if board[i][col] in s:
                    return False
                s.add(board[i][col])
        for square in range(9):
            s=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col=(square%3)*3+j
                    if board[row][col] ==".":
                        continue
                    if board[row][col] in s:
                        return False
                    s.add(board[row][col])
        return True
