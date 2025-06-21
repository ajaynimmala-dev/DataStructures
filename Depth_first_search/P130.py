class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j, board):
            print(i, j)
            board[i][j] = '.'
            for a, b in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + a
                y = j + b
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                    dfs(x, y, board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O':
                    dfs(i, j, board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    board[i][j] = 'O'



