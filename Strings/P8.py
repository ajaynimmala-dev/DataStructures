class Solution:
    def myAtoi(self, s: str) -> int:
        res=0
        i=0
        sign=0
        while i<len(s) and s[i]==' ':
            i+=1
        if(i==len(s)):
            return res
        else:
            if s[i]=='-':
                sign=1
                i+=1
            else:
                if s[i]=='+':
                    sign=0
                    i+=1
            if True:
                while i<len(s) and s[i].isdigit() != False:
                    res=res*10+int(s[i])
                    i+=1
                if sign==1:
                    res=-res
                    if(res<-2147483648):
                        return -2147483648
                    else:
                        return res
                else:
                    if res>2147483647:
                        return 2147483647
                    else:
                        return res