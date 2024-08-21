class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def isvalid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return (False)

            for i in range(9):
                if board[i][col] == num:
                    return (False)
            row_start = row - row % 3
            col_start = col - col % 3

            for i in range(3):
                for j in range(3):
                    if [row_start + i][col_start + j] == num:
                        return (False)
            return (True)

        row = 0
        col = 0
        while row < 9:
            for i in range(1, 10):
                if isvalid(board, row, col, str(i)):
                    board[row][col] = str(i)
                    col += 1
                col = 0
            row += 1