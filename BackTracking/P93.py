class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12:
            return []
        else:
            res=[]
            self.s=s
            def solve(j,c,curr):
                print(j,curr)
                if c==4:
                    if j==len(s):
                        res.append(curr[:-1])
                    else:
                        return
                if c>4:
                    return
                else:
                    for i in range(j,min(j+3,len(s))):
                        if int(s[j:i+1])<256 and (i==j or s[j] != '0'):
                            solve(i+1,c+1,curr+s[j:i+1]+'.')
            solve(0,0,'')
            return res