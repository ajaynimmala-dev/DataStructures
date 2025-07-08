class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)

        n = len(grid[0])

        res = [[0] * (n) for _ in range(m)]

        res[0][0] = grid[0][0]

        for i in range(1, m):
            res[i][0] = res[i - 1][0] + grid[i][0]

        for j in range(1, n):
            res[0][j] = res[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[-1][-1]