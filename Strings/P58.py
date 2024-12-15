class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        count=0
        while i<len(s):
            if s[i]!=' ':
                count+=1
                i+=1
            else:
                while i<len(s) and s[i]==' ':
                    i+=1
                if i==len(s):
                    return(count)
                else:
                    count=0
        return(count)
