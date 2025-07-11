class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        def solve(i,curr):
            if i==len(s):
                res.append(curr[:-1])
            if i>len(s):
                return
            else:
                for j in range(i,len(s)):
                    if s[i:j+1] in wordDict:
                        solve(j+1,curr+s[i:j+1]+' ')
        solve(0,'')
        return res