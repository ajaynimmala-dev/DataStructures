class Solution:
    def climbStairs(self, n: int) -> int:

        data = {}
        count = 0

        def solve(i, count):
            if i == n:
                count += 1
                return count
            elif i in data:
                return data[i]
            elif i > n:
                return 0
            else:
                data[i] = solve(i + 1, count) + solve(i + 2, count)
                return data[i]

        return solve(0, count)