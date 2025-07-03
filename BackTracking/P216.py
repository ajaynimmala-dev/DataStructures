class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        sub = []

        def solve(sub, res, j):
            if sum(sub) == n and len(sub) == k:
                res.append(sub.copy())
            else:
                for i in range(j, 10):
                    sub.append(i)
                    solve(sub, res, i + 1)
                    sub.pop()

        solve(sub, res, 1)
        return res
