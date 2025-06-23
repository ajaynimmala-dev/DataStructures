class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def solve(curr, open_, close_, res):
            if open_ == close_ == n:
                res.append(curr)
            else:
                # print(curr)
                if open_ < n:
                    solve(curr + '(', open_ + 1, close_, res)
                if open_ > close_:
                    solve(curr + ')', open_, close_ + 1, res)

        solve('', 0, 0, res)
        return res