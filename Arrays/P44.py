class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        t=0
        for x in p:
            indx=p.index(x)
            if x=='*':
                l=len(s)-1-t
                k=len(p)-(p.index(x))-1
                t=t+l-k+1
                continue
                return(True)
            if x==s[t]:
                t+=1
                continue
            if x=='?' and ord(s[t])>=97:
                t+=1
                continue
            else:
                return(False)
        if t<len(s):
            return(False)
        else:
            return(True)