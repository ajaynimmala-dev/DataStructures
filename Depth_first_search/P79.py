class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def solve(i, j, k, word):
            if i < 0 or j < 0:
                return False
            if k >= len(word):
                return True
            if i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] == '!':
                return False
            else:
                c = board[i][j]
                if c == word[k]:
                    board[i][j] = '!'
                    t1 = solve(i - 1, j, k + 1, word)
                    t2 = solve(i + 1, j, k + 1, word)
                    t3 = solve(i, j - 1, k + 1, word)
                    t4 = solve(i, j + 1, k + 1, word)
                    if t1 or t2 or t3 or t4:
                        return True
                    else:
                        board[i][j] = c
                        return False
                else:
                    return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if solve(i, j, 0, word):
                        return True
        return False

