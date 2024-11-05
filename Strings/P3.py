class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[0]
        temp=[]
        def solve(i,s,temp):
            temp.clear()
            while i!=len(s):
                if s[i] not in temp:
                    temp.append(s[i])
                else:
                    return(len(temp))
                i+=1
            return(len(temp))
        i=0
        while(i!=len(s)):
            res.append(solve(i,s,temp))
            i+=1
        return(max(res))