class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dp(i, words):
            f = [False for _ in range(len(s) + 1)]
            f[0] = True
            for i in range(len(s) + 1):
                for j in range(i):
                    if f[j] == True and s[j:i] in words:
                        f[i] = True
            return f[-1]

        words = {i for i in wordDict}
        return dp(0, words)