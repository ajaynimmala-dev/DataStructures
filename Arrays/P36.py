class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """check if the given matrix is valid or not"""

        def row_check(r, board):
            res = []
            for i in range(0, 9):
                if board[r][i] != '.':
                    if board[r][i] not in res:
                        res.append(board[r][i])
                    else:
                        return (False)
            return (True)

        def col_check(c, board):
            res = []
            for i in range(0, 9):
                if board[i][c] != '.':
                    if board[i][c] not in res:
                        res.append(board[i][c])
                    else:
                        return (False)
            return (True)

        def matrix(row, col, board):
            res = []
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] != '.':
                        if board[i][j] not in res:
                            res.append(board[i][j])
                        else:
                            return (False)
            return (True)

        for i in range(0, 9):
            res = row_check(i, board)
            if res == False:
                return (False)
        for i in range(0, 9):
            res = col_check(i, board)
            if res == False:
                return (False)
        row = 0
        while row < 9:
            col = 0
            while col < 9:
                res = matrix(row, col, board)
                if res == False:
                    return (False)
                else:
                    col += 3
            row += 3
        return (True)
