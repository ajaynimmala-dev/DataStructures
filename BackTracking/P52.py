class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [['.' for i in range(n)] for k in range(n)]
        res = []

        def check(r, c, board):
            for i in range(c):
                if board[r][i] == '1' or board[r][i] == 'Q':
                    return False
            for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
                if board[i][j] == '1' or board[i][j] == 'Q':
                    return False

            for i, j in zip(range(r, len(board)), range(c, -1, -1)):
                if board[i][j] == '1' or board[i][j] == 'Q':
                    return False
            return True

        def solve(c, board):
            if c >= len(board):
                j = 0
                temp = board[:]
                for i in temp:
                    temp[j] = ''.join(i)
                    j += 1
                if temp not in res:
                    res.append(temp[:])
                    solve(0, board)
                    return True
                return True
            else:
                for i in range(len(board)):
                    if (check(i, c, board)):
                        board[i][c] = 'Q'
                        if solve(c + 1, board):
                            return True
                        else:
                            board[i][c] = '.'
                return False

        solve(0, board)
        return len(res)
