class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = a + i
                y = b + j
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    check(x, y)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    check(i, j)
                    count += 1
        return count

