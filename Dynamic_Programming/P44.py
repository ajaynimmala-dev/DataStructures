class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res=[ [False]*(len(p)+1) for _ in range(len(s)+1)]
        res[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1] == '*':
                res[0][i] = res[0][i-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1].isalpha():
                    if p[j-1] == s[i-1]:
                        res[i][j] = res[i-1][j-1]
                elif p[j-1] == '?':
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j]= res[i][j-1] or res[i-1][j]
        return res[-1][-1]
