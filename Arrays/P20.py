class Solution:
    def isValid(self, s: str) -> bool:
        p1,p2,s1,s2,f1,f2=('(',')','['.']','{','}')
        for i in s:
            if i==p1:
                if p2 in s:
                    pass
                else:
                    return("false")

