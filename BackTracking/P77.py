class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sub = []
        res = []

        def solve(j, sub, res):
            if len(sub) == k:
                res.append(sub[:])
            else:
                for i in range(j, n + 1):
                    if i not in sub:
                        sub.append(i)
                        solve(i, sub, res)
                        sub.pop()

        solve(1, sub, res)
        return res

