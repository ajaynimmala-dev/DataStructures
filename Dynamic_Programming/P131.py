class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispalidrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def solve(l, start, res, sub):
            if start == l:
                res.append(sub.copy())
            else:
                for i in range(start, l):
                    temp = s[start:i + 1]
                    if ispalidrome(temp):
                        sub.append(temp)
                        solve(l, i + 1, res, sub)
                        sub.pop()

        solve(len(s), 0, res, [])
        return res