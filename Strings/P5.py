class Solution:
    def longestPalindrome(self, s: str) -> str:
        start,end=(0,0)
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if i==0 and s[i:j+1]==s[j::-1] and abs(start-end)<len(s[i:j+1:1]):
                    start,end=(i,j)
                else:
                    if s[i:j+1:1]==s[j:i-1:-1] and abs(start-end)<len(s[i:j+1:1]):
                        start,end=(i,j)
        return(s[start:end+1])