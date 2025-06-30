class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        r = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []

        def solve(c, indi):
            if indi >= len(digits):
                res.append(c)
                return
            else:
                for i in range(len(r[digits[indi]])):
                    temp = c
                    c = c + r[digits[indi]][i]
                    solve(c, indi + 1)
                    c = temp

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return r[digits[0]]
        else:
            for i in range(len(r[digits[0]])):
                solve(r[digits[0]][i], 1)
        return res















